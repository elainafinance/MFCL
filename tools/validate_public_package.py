from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class DemoParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.page_ids: set[str] = set()
        self.nav_targets: set[str] = set()
        self.external_assets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        classes = (values.get("class") or "").split()
        if tag == "section" and "page" in classes and values.get("id"):
            self.page_ids.add(values["id"] or "")
        if values.get("data-page"):
            self.nav_targets.add(values["data-page"] or "")
        for name in ("src", "href"):
            value = values.get(name) or ""
            if value.startswith(("http://", "https://", "//")):
                self.external_assets.append(value)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def markdown_links() -> list[tuple[Path, str]]:
    broken: list[tuple[Path, str]] = []
    pattern = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
    for source in ROOT.rglob("*.md"):
        text = source.read_text(encoding="utf-8")
        for target in pattern.findall(text):
            if target.startswith(("http://", "https://", "#")):
                continue
            resolved = (source.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                broken.append((source.relative_to(ROOT), target))
    return broken


def main() -> int:
    required = [
        "README.md", "index.html", "PUBLISHING.md", "VALIDATION.md",
        "architecture/data-flow.md", "architecture/agent-map.md",
        "architecture/approval-flow.md", "agents/README.md",
        "controls/README.md", "demo/README.md", "case-study/README.md",
        "case-study/Municipal_Finance_Control_Layer_LinkedIn_Case_Study.pdf",
    ]
    check(all((ROOT / item).exists() for item in required), "required public file missing")

    source = (ROOT / "index.html").read_text(encoding="utf-8")
    parser = DemoParser()
    parser.feed(source)
    check(len(parser.ids) == len(set(parser.ids)), "duplicate HTML ID")
    check(len(parser.page_ids) == 20, "expected 20 public demo pages")
    check(parser.page_ids == parser.nav_targets, "navigation and page targets differ")
    check(not parser.external_assets, "demo requires an external asset")

    required_controls = {
        "guidedDemoBtn", "syncBtn", "processRevenueBtn", "bankReconBtn",
        "integrityCaseBtn", "splostControlBtn", "interfundSettlementBtn",
        "spendControlBtn", "payrollRunBtn", "payrollRange", "payrollChangeBtn",
        "payrollVerifyBtn", "departmentRefreshBtn", "sefaAssembleBtn",
        "assemblyBtn", "noteDraftBtn", "complianceBtn", "intakeBtn",
        "registryBtn", "selfApproveBtn", "authorizedApproveBtn", "dryRunBtn",
        "reuseAuthBtn", "changePayloadBtn", "technicalBtn", "traceEventBtn",
        "reportBtn",
    }
    check(required_controls.issubset(set(parser.ids)), "interactive control missing")

    prohibited = ["file:///", "mfcl_qbd_sandbox", "private-output", "private-input"]
    public_text_files = [
        path for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".html", ".txt"}
        and path.name not in {".gitignore"}
    ]
    combined = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in public_text_files).lower()
    check(not [term for term in prohibited if term in combined], "internal path or private-folder marker found")
    check(not markdown_links(), "broken relative Markdown link")

    pdf = ROOT / "case-study/Municipal_Finance_Control_Layer_LinkedIn_Case_Study.pdf"
    check(pdf.stat().st_size > 50_000, "case-study PDF is missing or unexpectedly small")
    check(all(path.stat().st_size > 25_000 for path in (ROOT / "demo/screenshots").glob("*.png")), "screenshot missing or unexpectedly small")

    print("MFCL_PUBLIC_PACKAGE_VALIDATION=PASS")
    print(f"PUBLIC_DEMO_PAGES={len(parser.page_ids)}")
    print(f"EXTERNAL_ASSETS={len(parser.external_assets)}")
    print(f"INTERACTIVE_CONTROLS={len(required_controls)}")
    print("BROKEN_RELATIVE_LINKS=0")
    print("INTERNAL_PATH_MARKERS=0")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"MFCL_PUBLIC_PACKAGE_VALIDATION=FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
