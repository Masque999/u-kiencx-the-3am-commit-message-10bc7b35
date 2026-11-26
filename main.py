#!/usr/bin/env python3
"""The 3AM Commit Message: write one funny commit message to /output/entry.txt."""
import os

LINE = "fix: 3am, changed one line and the tests pass; no idea why, too afraid to ask"

assert 1 <= len(LINE) <= 139, f"line must be 1-139 chars, got {len(LINE)}"
assert LINE == LINE.strip(), "no leading/trailing whitespace"
assert "\n" not in LINE, "must be a single line"
assert LINE.strip(), "must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not pass quietly.
with open("/output/entry.txt", encoding="utf-8") as f:
    back = f.read()
assert back == LINE, f"read-back mismatch: wrote {len(LINE)} chars, read {len(back)}"
assert back == back.strip() and "\n" not in back, "read-back failed line checks"

print(f"wrote {len(LINE)} chars to /output/entry.txt")
