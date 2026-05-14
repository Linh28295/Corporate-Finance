# models/builds/

Populated, working financial models with real company financials — the analytical engine of the project.

## What belongs here

- **Stage 3 populated model** — the ratio template filled with audited financials for the selected company, with all ratios auto-computing

## Files

| File | Company | Stage | Years |
|------|---------|-------|-------|
| `2026-05-10-coca-cola-financials.xlsx` | The Coca-Cola Company (KO) | Stage 3 | FY2025 + FY2024 |

## Naming convention

```
YYYY-MM-DD-{company-slug}-financials.xlsx
```

**Example:** `2026-05-10-coca-cola-financials.xlsx`

## Requirements before committing

- Both FY2025 (current) and FY2024 (prior year / `startYear_*`) columns populated
- Cover & Instructions tab updated: company, ticker, exchange, currency, units, reporting standard, fiscal year end, source URL
- No `#REF!`, `#DIV/0!`, or `#NAME?` errors on the Ratios tab
- Balance sheet balances both years: Total Assets = Total Liabilities + Equity
