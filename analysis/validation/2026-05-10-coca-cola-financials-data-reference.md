# Stage 3 — Coca-Cola Financial Data Reference
## The Coca-Cola Company (KO) | FY2024 & FY2023

**Source:** Mergent Online 5-Year Summary | As Originally Reported  
**Units:** USD Millions throughout  
**Reporting Standard:** U.S. GAAP  
**Fiscal Year End:** December 31  
**Template target file:** `models/builds/2026-05-10-coca-cola-financials.xlsx`

> Use this document side-by-side with the Excel template. Enter every number exactly as shown. Verify the Balance Sheet check at the end before uploading.

---

## COVER & INSTRUCTIONS TAB

| Field | Value |
|-------|-------|
| Company Name | The Coca-Cola Company |
| Ticker | KO |
| Exchange | NYSE |
| Reporting Currency | USD |
| Units | Millions |
| Reporting Standard | U.S. GAAP |
| Fiscal Year End | December 31 |
| Current Year | FY2024 (ended Dec 31, 2024) |
| Prior Year | FY2023 (ended Dec 31, 2023) |
| Source | Mergent Online / KO 10-K via SEC EDGAR |
| Analyst | Nguyen Bui Ngoc Linh |
| Date Populated | 2026-05-10 |
| Notes | Retained earnings (Reinvested earnings) are POSITIVE. Large treasury stock (-$55,916M) and AOCI (-$16,779M) reduce total equity. Equity method investments ($18,087M) are material non-current assets. |

---

## INCOME STATEMENT TAB

Source: Consolidated Statements of Income

| Line Item | FY2024 | FY2023 |
|-----------|-------:|-------:|
| **Net Operating Revenues (Total Revenue)** | **47,061** | **45,754** |
| Cost of Goods Sold (Cost of Revenue) | 18,324 | 18,520 |
| **Gross Profit** | **28,737** | **27,234** |
| Selling, General & Administrative Expenses | 14,582 | 13,972 |
| Unusual Expense / (Income) | (654) | (228) |
| Other Operating Expenses | 3,109 | 1,702 |
| **Total Operating Expenses** | **35,361** | **33,981** |
| **Operating Income (EBIT)** | **11,700** | **11,773** |
| Interest Income / (Expense), Net | 1,417 | 1,256 |
| Other, Net | (31) | (77) |
| **Net Income Before Taxes (EBT)** | **13,086** | **12,952** |
| Provision for Income Taxes | 2,437 | 2,249 |
| **Net Income** | **10,631** | **10,714** |
| | | |
| Basic EPS | 2.47 | 2.48 |
| Diluted EPS | 2.46 | 2.47 |
| Basic Weighted Average Shares (millions) | 4,309 | 4,323 |
| Diluted Weighted Average Shares (millions) | 4,320 | 4,339 |
| Dividends Per Share | 1.965 | 1.865 |
| Effective Tax Rate | 18.62% | 17.36% |

**Notes:**
- Interest figure shown is **net** (income minus expense). If the template has separate rows, source the gross split from the 10-K footnotes
- Unusual Expense is **negative** (income) in FY2024 due to asset gains — enter as shown

---

## BALANCE SHEET TAB

Source: Consolidated Balance Sheets  
⚠️ Enter **both columns**: FY2024 = current year | FY2023 = prior year (`startYear_*`)

### ASSETS

| Line Item | FY2024 (Dec 31) | FY2023 (Dec 31) |
|-----------|----------------:|----------------:|
| **CURRENT ASSETS** | | |
| Cash & Cash Equivalents | 10,828 | 9,366 |
| Short-term Investments (incl. in Cash line above) | 3,743 | 4,297 |
| *Cash, Cash Equiv. & Short-term Investments (total)* | *14,571* | *13,663* |
| Total Receivables, Net | 3,569 | 3,410 |
| Inventories | 4,728 | 4,424 |
| Prepaid Expenses & Other Current Assets | 2,998 | 3,141 |
| Other Current Assets | 131 | 2,094 |
| **Total Current Assets** | **25,997** | **26,732** |
| | | |
| **NON-CURRENT ASSETS** | | |
| Property, Plant & Equipment — Gross | 21,055 | 19,797 |
| Accumulated Depreciation | (9,570) | (9,233) |
| **PP&E — Net** | **11,485** | **10,564** |
| Goodwill | 18,139 | 18,358 |
| Other Intangible Assets, Net | 13,301 | 14,865 |
| Long-term / Equity Method Investments | 18,087 | 19,789 |
| Other Long-term Assets | 13,540 | 7,395 |
| **Total Assets** | **100,549** | **97,703** |

### LIABILITIES

| Line Item | FY2024 (Dec 31) | FY2023 (Dec 31) |
|-----------|----------------:|----------------:|
| **CURRENT LIABILITIES** | | |
| Accounts Payable | 5,468 | 5,590 |
| Accrued Expenses | 16,244 | 9,176 |
| Current Portion of Long-term Debt | 648 | 1,960 |
| Notes Payable / Short-term Debt | 1,499 | 4,557 |
| Other Current Liabilities | 1,390 | 2,288 |
| **Total Current Liabilities** | **25,249** | **23,571** |
| | | |
| **NON-CURRENT LIABILITIES** | | |
| Long-term Debt | 42,375 | 35,547 |
| Deferred Income Tax Liabilities | 2,469 | 2,639 |
| Other Long-term Liabilities | 4,084 | 8,466 |
| Minority / Noncontrolling Interest | 1,516 | 1,539 |
| **Total Liabilities** | **75,693** | **71,762** |

### EQUITY

| Line Item | FY2024 (Dec 31) | FY2023 (Dec 31) |
|-----------|----------------:|----------------:|
| Common Stock | 1,760 | 1,760 |
| Additional Paid-in Capital (APIC) | 19,801 | 19,209 |
| Retained Earnings (Reinvested Earnings) — **POSITIVE** | 76,054 | 73,782 |
| Treasury Stock — enter as **NEGATIVE** | (55,916) | (54,535) |
| Accumulated Other Comprehensive Income (Loss) | (16,779) | (14,274) |
| **Total Equity (attributable to KO shareholders)** | **24,856** | **25,941** |
| | | |
| **Total Liabilities & Shareholders’ Equity** | **100,549** | **97,703** |
| Total Common Shares Outstanding (millions) | 4,302 | 4,308 |

**Balance check:**
- FY2024: $100,549 = $75,693 + $24,856 ✅
- FY2023: $97,703 = $71,762 + $25,941 ✅

---

## CASH FLOW TAB

Source: Consolidated Statements of Cash Flows

| Line Item | FY2024 | FY2023 |
|-----------|-------:|-------:|
| **OPERATING ACTIVITIES** | | |
| Net Income (consolidated) | 10,649 | 10,703 |
| Changes in Working Capital | (6,234) | (846) |
| **Net Cash from Operating Activities (CFO)** | **6,805** | **11,599** |
| | | |
| **INVESTING ACTIVITIES** | | |
| Capital Expenditures — enter as **NEGATIVE** | (2,064) | (1,852) |
| Investment Purchases / (Sales), Net | 235 | 366 |
| Sale of Fixed Assets | 40 | 74 |
| Acquisition of Business | (315) | (62) |
| Sale / Maturity of Investments | 6,589 | 4,354 |
| Other Investing Cash Flow | 4,588 | (1,497) |
| **Net Cash from Investing Activities (CFI)** | **2,524** | **(3,349)** |
| | | |
| **FINANCING ACTIVITIES** | | |
| Issuance / (Retirement) of Debt, Net | 2,528 | 1,857 |
| Issuance / (Retirement) of Stock, Net | (1,048) | (1,750) |
| Total Cash Dividends Paid — enter as **NEGATIVE** | (8,359) | (7,952) |
| **Net Cash from Financing Activities (CFF)** | **(6,910)** | **(8,310)** |
| | | |
| Foreign Exchange Effects on Cash | (623) | (73) |
| **Net Change in Cash** | **1,796** | **(133)** |
| Beginning Cash Balance | 9,692 | 9,825 |
| Ending Cash Balance | 11,488 | 9,692 |

---

## MARKET & ASSUMPTIONS INPUTS

| Input | FY2024 | FY2023 | Source |
|-------|-------:|-------:|--------|
| KO Share Price (Dec 31) | ~$62.00 | ~$58.90 | Yahoo Finance / Bloomberg |
| Diluted Shares Outstanding (millions) | 4,320 | 4,339 | 10-K EPS note |
| Market Capitalization (USD millions) | ~267,600 | ~255,750 | Price × Shares |
| Effective Tax Rate | 18.62% | 17.36% | Income Tax footnote, 10-K |
| EBITDA | 12,121 | 12,673 | Mergent Ratio section |
| Free Cash Flow | 4,741 | 9,747 | Mergent Ratio section |

> ⚠️ Verify the share price with Yahoo Finance for the exact Dec 31 closing price

---

## PRE-UPLOAD SELF-CHECK

- [ ] **Balance Sheet balances both years:** $100,549M (FY2024) and $97,703M (FY2023)
- [ ] **No formula errors** on Ratios tab (`#REF!`, `#DIV/0!`, `#NAME?`)
- [ ] **Prior year column** (`startYear_*`) fully populated with FY2023 figures
- [ ] **Treasury stock** entered as negative in both years
- [ ] **AOCI** entered as negative in both years
- [ ] **Capex** entered as negative
- [ ] **Dividends paid** entered as negative
- [ ] **Cover tab** completed with source, standard (U.S. GAAP), currency (USD), FYE (Dec 31)
- [ ] File saved as: `models/builds/2026-05-10-coca-cola-financials.xlsx`
- [ ] Commit message: `Populate Coca-Cola FY2024 + FY2023 financials from Mergent 10-K source`

---

## SELECTED RATIO BENCHMARKS (from Mergent — for Ratios tab verification)

Use these to spot-check your auto-computed Ratios tab:

| Ratio | FY2024 | FY2023 |
|-------|-------:|-------:|
| Gross Margin | 61.1% | 59.5% |
| Operating Margin | 24.9% | 25.7% |
| Net Profit Margin | 22.6% | 23.4% |
| EBITDA Margin | 27.2% | 28.2% |
| Current Ratio | 1.03 | 1.13 |
| Quick Ratio | 0.84 | 0.95 |
| Total Debt / Total Equity | 176.5% | 154.6% |
| Long-term Debt / Capital | 61.6% | 56.4% |
| Interest Coverage | 7.5x | 7.0x |
| Asset Turnover | 0.468 | 0.468 |
| Days Inventory (DOH) | 94 | 87 |
| Days Receivable (DSO) | 28 | 27 |
| Days Payable (DPO) | 109 | 110 |
| Free Cash Flow (USD M) | 4,741 | 9,747 |
| Return on Equity (normalized) | 38.8% | 40.6% |
| Return on Assets (normalized) | 9.9% | 10.8% |
