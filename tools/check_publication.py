#!/usr/bin/env python3
"""Narrow public-release check. This is NOT a security audit or secret scanner."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
excluded = {".git", "__pycache__", "node_modules", "build", "coverage"}
allowed_ext = {".md", ".sol", ".py", ".gitignore", ""}
errors = []
files = []

for p in sorted(root.rglob("*")):
    if not p.is_file() or any(part in excluded for part in p.relative_to(root).parts):
        continue
    files.append(p)
    rel = p.relative_to(root)
    if p.suffix not in allowed_ext:
        errors.append(f"Unexpected file type (review for sensitive binary content): {rel}")
        continue
    try:
        data = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"File is not UTF-8 text: {rel}")
        continue
    # Ethereum addresses and full transaction hashes can correlate a deployer to an identity.
    for pattern, description in [
        (r"\b0x[a-fA-F0-9]{40}\b", "Ethereum address"),
        (r"\b0x[a-fA-F0-9]{64}\b", "transaction/hash identifier"),
    ]:
        if re.search(pattern, data):
            errors.append(f"{rel}: public {description} needs explicit disclosure approval")

source = (root / "src" / "HitCoin.sol").read_text(encoding="utf-8")
checks = {
    "MIT SPDX": "// SPDX-License-Identifier: MIT" in source,
    "historical solidity pragma": "pragma solidity ^0.8.20;" in source,
    "token identity": 'ERC20("Hit Coin", "HIT")' in source,
    "fixed initial supply": "_mint(owner, 1000000000000 * 10 ** decimals())" in source,
    "no externally callable mint": re.search(r"function\s+mint\s*\(", source) is None,
}
errors.extend(name for name, ok in checks.items() if not ok)
if errors:
    print("PUBLICATION CHECK FAILED:")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"PASS: {len(files)} curated files, {len(checks)} source checks, no exposed Ethereum addresses or full tx hashes detected")
print("NOTE: this does not replace an independent privacy/security or smart-contract review.")
