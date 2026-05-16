# analysis/validation/

Self-audit reports, data reference documents, and validation documentation for Stage 3 model population.

## Files

| File | Description |
|------|-------------|
| `2026-05-10-coca-cola-financials-data-reference.md` | Complete FY2025 + FY2024 financial data reference — all IS, BS, CFS figures with balance checks confirmed |
| `2026-05-10-coca-cola-stage3-data-guide.md` | Named range mapping guide — links each `INC_*`, `BAL_*`, `CASH_*` range to its 10-K line item with actual values |

## Validation results (Stage 3)

| Check | Result |
|-------|--------|
| Balance Sheet FY2025 | $104,816M = $72,647M + $32,169M ✅ |
| Balance Sheet FY2024 | $100,549M = $75,693M + $24,856M ✅ |
| Du Pont ROA | 0.477 × 0.302 = 14.4% ≈ direct ROA 14.4% ✅ |
| No formula errors | Zero #REF!, #DIV/0!, #NAME? ✅ |
| All named ranges populated | 90 / 90 cells non-empty ✅ |
| Sign checks | No impossible negatives ✅ |

## Naming convention

```
YYYY-MM-DD-{company-slug}-{descriptor}.md
```
