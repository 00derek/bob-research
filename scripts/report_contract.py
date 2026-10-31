"""Portable framework-report contract, also shipped with the public validator.

Structural coverage is not verification of the underlying investment evidence.
"""
from __future__ import annotations

import re

PRIVATE_TEXT = re.compile(
    r"\b(?:portfolio|broker(?:age)?|orchestrator|account|IRA|Derek|"
    r"(?:actual|personal|my|our)\s+NAV|"
    r"cost basis|average.cost|reference.shares?|shares held|held shares|"
    r"protected.floor|profit.floor|live.floor|our position|my position|"
    r"held|inactive|watchlist|unreconciled|my|our|I own|I hold|exit fill|"
    r"prior exit|inherited EXIT|target remains unresolved|"
    r"position size|planned size|incremental (?:weight|risk|allocation)|"
    r"not.held|holdings ledger|reconciled shares|last[- ]verified|reference NAV|"
    r"mixed.date|existing factor sleeve|existing shares|direct technology book|"
    r"inherited (?:unresolved )?(?:exit|floor|stop|target)|"
    r"legacy (?:exit|stop|target)|historical exit|flat status|holding-specific|shadow add|"
    r"current stage/shares|current NAV and position|reconciled (?:\d|flat|position)|"
    r"unresolved [^.\n]{0,45}(?:floor|stop|target)|"
    r"direct [^.\n]{0,65}positions|proposed\s+\d[\d,.]*%?\s+NAV|"
    r"predeclared combined [^.\n]{0,40}policy band)\b|"
    r"\b\d[\d,]*(?:\.\d+)?\s+(?:dated\s+)?shares\b|"
    r"portfolio|brokerage|orchestrator|unheld|holding-specific|BLOCKED_[A-Z_]+|"
    r"shadow (?:add|increment)|existing order/fill|PriorEXIT|currentexitstate|legacyexit|"
    r"holding-appropriate|new holding risk map|priorunresolved|unresolvedexit|"
    r"accountstate|legacyunresolved|unresolvedstate|Reconcilepriororders|"
    r"existing holdings|direct [^.\n]{0,65}sleeve|combined\s+VTI/VOO|"
    r"current[≤<][^.\n]{0,40}target|unresolved Exit|NOT_REQUIRED|PENDING_ORCHESTRATOR|"
    r"reconciled\s*\d|/Users/|file://", re.I)

COMPANY_SECTIONS = (
    ("decision", "Decision and thesis"),
    ("macro", "Macro transmission"),
    ("industry", "Industry and competitive structure"),
    ("business", "Business and growth architecture"),
    ("financials", "Financial health and capital allocation"),
    ("valuation", "Valuation and scenarios"),
    ("reverse", "Reverse valuation"),
    ("catalysts", "Catalysts and sentiment"),
    ("technicals", "Technical timing"),
    ("risks", "Risks and thesis invalidation"),
    ("levels", "Entry and exit map"),
    ("sources", "Evidence and sources"),
)
FUND_SECTIONS = (
    ("decision", "Decision and role"),
    ("macro", "Macro and market context"),
    ("mandate", "Mandate and process"),
    ("holdings", "Holdings and concentration"),
    ("costs", "Costs liquidity and tracking"),
    ("valuation", "Look-through valuation"),
    ("integrity", "Vehicle integrity"),
    ("technicals", "Catalysts and technical timing"),
    ("risks", "Risk and rebalance rules"),
    ("sources", "Evidence and sources"),
)
STATUSES = {"DOCUMENTED", "PARTIAL", "GAP", "NOT_APPLICABLE"}
KINDS = {"FRAMEWORK_ANALYSIS", "RECONSTRUCTED_RESEARCH"}
FORMATS = {"framework-v1", "reader-v2"}


def sections(instrument_type):
    return COMPANY_SECTIONS if instrument_type == "OPERATING_COMPANY" else FUND_SECTIONS


def coverage_errors(params, body):
    report_format = params.get("report_format")
    if report_format is None:
        return []  # Immutable legacy revisions retain their original format.
    if report_format not in FORMATS:
        return ["Unknown report format."]
    reader = report_format == "reader-v2"
    errors = []
    expected = sections(params.get("instrument_type"))
    coverage = params.get("coverage")
    if not isinstance(coverage, list) or len(coverage) != len(expected):
        return ["Framework coverage must include every applicable section."]
    if params.get("report_kind") not in KINDS:
        errors.append("Unknown framework report kind.")
    headings = re.findall(r"^## (.+)$", body, re.M)
    if reader:
        if (not headings or headings[0] != "Investment thesis" or
                headings[-1] != "Evidence and sources" or
                "Framework assessment" not in headings or len(set(headings)) != len(headings)):
            errors.append("Reader report needs a unique Investment thesis first, Framework assessment, and Evidence and sources last.")
        for field in ("company_name", "thesis_headline"):
            value = params.get(field)
            if not isinstance(value, str) or not value.strip() or "\n" in value:
                errors.append(f"Reader report needs a one-line {field}.")
    elif headings != [title for _, title in expected]:
        errors.append("Framework sections are missing, duplicated or out of order.")
    chunks = re.split(r"^## .+$", body, flags=re.M)[1:]
    chapter_text = dict(zip(headings, chunks))
    if reader:
        for title in ("Investment thesis", "Framework assessment", "Evidence and sources"):
            if len(chapter_text.get(title, "").strip()) < 80:
                errors.append(f"{title} needs substantive explanation, not only a heading.")
    for index, ((key, title), entry) in enumerate(zip(expected, coverage)):
        required = {"id", "status", "note", "section"} if reader else {"id", "status", "note"}
        if not isinstance(entry, dict) or set(entry) != required:
            errors.append(f"Invalid coverage record for {title}.")
            continue
        if entry["id"] != key or entry["status"] not in STATUSES or not isinstance(entry["note"], str) or not entry["note"].strip():
            errors.append(f"Invalid coverage status or explanation for {title}.")
        if reader:
            section = entry.get("section")
            if not isinstance(section, str) or section not in chapter_text:
                errors.append(f"{title} must link to an existing report section.")
                continue
            text = chapter_text[section].strip()
        else:
            text = chunks[index].strip() if index < len(chunks) else ""
        if text:
            if len(text) < 80:
                errors.append(f"{title} needs reasoning or an explicit evidence-gap explanation.")
            if entry["status"] in {"PARTIAL", "GAP"} and "Evidence gap:" not in text:
                errors.append(f"{title} must disclose its evidence gap in the report body.")
        else:
            errors.append(f"{title} needs reasoning or an explicit evidence-gap explanation.")
    if not re.search(r"https?://", chunks[-1] if chunks else ""):
        errors.append("Evidence and sources needs publicly addressable source links.")
    return errors
