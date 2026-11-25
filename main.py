"""One-line office joke entry for make.fun.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt with no trailing newline.
"""

import os

ENTRY = "My coworker starts every email 'per my last email', so I replied 'per my last email, I never read your last email.'"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
