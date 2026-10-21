"""Public artifact checks; no dependency on the private agent workspace."""
import hashlib
import json
from pathlib import Path
import re
import sys
from report_contract import coverage_errors, PRIVATE_TEXT


def check(root):
    errors = []
    manifest = json.loads((root / "publication.json").read_text())["files"]
    for name, expected in manifest.items():
        p = root / name
        if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):
            errors.append("Unsafe export path: " + name)
        elif not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != expected:
            errors.append("Export digest mismatch: " + name)
    for p in (root / "content/research").rglob("*.md"):
        if p.name == "_index.md":
            continue
        raw = p.read_text()
        try:
            meta, end = json.JSONDecoder().raw_decode(raw)
            params = meta["params"]
            if not all(params.get(k) for k in ("ticker", "report_id", "framework_version", "security_signal", "evidence_status")):
                errors.append("Missing report fields: " + str(p))
            if not raw[end:].strip():
                errors.append("Empty report: " + str(p))
            errors.extend(f"{p}: {error}" for error in coverage_errors(params, raw[end:].strip()))
            if PRIVATE_TEXT.search(raw):
                errors.append("Private context in report: " + str(p))
        except (ValueError, KeyError, TypeError):
            errors.append("Invalid report metadata: " + str(p))
    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts or p.suffix not in {".md", ".json", ".toml", ".html", ".js", ".css", ".yml", ".py"}:
            continue
        if re.search(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----", p.read_text()):
            errors.append("Credential pattern: " + str(p))
    return errors


if __name__ == "__main__":
    failures = check(Path(sys.argv[1]).resolve())
    print("\n".join(failures) if failures else "Public artifact checks passed")
    raise SystemExit(bool(failures))
