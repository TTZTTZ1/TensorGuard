# Confirmed Bugs

This directory contains the 14 confirmed bug trigger examples listed in the appendix of `基于大语言模型的深度学习库模糊测试.pdf`.

The entries are separated from `reports/confirmed_bugs/` so that confirmed reference bugs and newly triaged project bugs do not get mixed.

Each bug directory contains:

- `meta.json`: structured metadata for the web UI and report generator.
- `repro.py`: minimal trigger code transcribed from the appendix.
- `report.md`: human-readable bug report draft.

The observed behavior is taken from the paper appendix. Re-running these cases should be done in isolated subprocesses because several triggers intentionally crash or abort the process.
