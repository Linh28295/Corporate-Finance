# tools/

Repository tooling — scripts the project uses to build deliverables that aren't authored by hand.

## Files

| Script | Builds | Run |
|---|---|---|
| `build_cv.py` | `deliverables/Nguyen-Bui-Ngoc-Linh-CV.pdf` (A4, two-page, ATS-friendly, Liberation Sans, navy-and-white) | `python3 tools/build_cv.py` |

## Dependencies

`build_cv.py` uses [ReportLab](https://www.reportlab.com/). Install once:

```bash
pip install reportlab
```

The script also expects the Liberation font family at `/usr/share/fonts/truetype/liberation/` (default on most Debian/Ubuntu systems; install with `apt install fonts-liberation` if missing).

## Conventions

- Each script is self-contained and idempotent — running it twice produces the same output bytes (modulo PDF stream metadata).
- Output paths are hard-coded relative to the repo root; run from the repo root.
- No content comes from external network calls — all strings the scripts emit live in this directory or are passed in via the source file the script renders.
