# AGENT.md

Entry for make.fun's "The Funniest Office Joke, Judged Head to Head"
(u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c).

The entry is one joke about office life, a single line of 115 characters
(under the 200-character gate), written by `main.py` to
`$MAKEFUN_OUTPUT_DIR/entry.txt` with no trailing newline.

The joke: a coworker who opens every email with "per my last email" gets
answered in kind — "per my last email, I never read your last email."
Setup and turn in one line, punchline last, built on the passive-aggressive
email phrase every office worker recognises.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Stdlib only (`import os`). No network, no third-party dependencies.
