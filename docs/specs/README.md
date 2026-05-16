# docs/specs/

Technical specifications that define analytical work precisely enough for any competent executor — human or AI — to produce correct output without additional context.

## Files

| File | Stage | Description |
|------|-------|-------------|
| `2026-05-16-nguyen-coca-cola-spec.md` | Stage 4 | Full 11-section technical specification for Coca-Cola ratio analysis |
| `2026-05-16-nguyen-coca-cola-prompt-log.md` | Stage 4 | Prompt log documenting LLM usage and design decisions |

## What belongs here

- **Stage 4 technical specifications** — the central project artifact. Each spec fully defines:
  - **Part A (Model Specification):** Spreadsheet architecture, all financial data inputs, named range conventions, ratio formulas, and validation rules
  - **Part B (Analysis Specification):** Interpretation requirements, benchmarks, strategic recommendation criteria, and output format
- **Prompt logs** — record of LLM prompts and design decisions for each spec

## Naming convention

```
YYYY-MM-DD-{lastname}-{company-slug}-spec.md
YYYY-MM-DD-{lastname}-{company-slug}-prompt-log.md
```

## Quality test

A well-written spec is **self-contained**. If you hand it to an LLM with zero additional context, they should produce a substantially correct ratio analysis. If they cannot, the spec has gaps.
