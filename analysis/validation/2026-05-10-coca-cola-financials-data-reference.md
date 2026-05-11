# Stage 3 — Coca-Cola Financial Data Reference
## The Coca-Cola Company (KO) | FY2025 & FY2024

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
| Current Year | FY2025 (ended Dec 31, 2025) |
| Prior Year | FY2024 (ended Dec 31, 2024) |
| Source | Mergent Online / KO 10-K via SEC EDGAR |
| Analyst | Nguyen Bui Ngoc Linh |
| Date Populated | 2026-05-10 |
| Notes | Treasury Stock (-$56,423M) and AOCI (-$14,105M) are large negatives that reduce equity. Equity method investments ($20,235M) are material non-current assets. Retained earnings are POSITIVE. |

---

## INCOME STATEMENT TAB

Source: Consolidated Statements of Income

| Line Item | FY2025 | FY2024 |
|-----------|-------:|-------:|
| **Net Operating Revenues (Total Revenue)** | **47,941** | **47,061** |
| Cost of Goods Sold (Cost of Revenue) | 18,397 | 18,324 |
| **Gross Profit** | **29,544** | **28,737** |
| Selling, General & Administrative Expenses | 14,521 | 14,582 |
| Unusual Expense / (Income) | 582 | (654) |
| Other Operating Expenses | 47 | 3,109 |
| **Total Operating Expenses** | **33,547** | **35,361** |
| **Operating Income (EBIT)** | **14,394** | **11,700** |
| Interest Income / (Expense), Net | 1,683 | 1,417 |
| Other, Net | (79) | (31) |
| **Net Income Before Taxes (EBT)** | **15,998** | **13,086** |
| Provision for Income Taxes | 2,861 | 2,437 |
| **Net Income** | **13,107** | **10,631** |
| | | |
| Basic EPS | 3.05 | 2.47 |
| Diluted EPS | 3.04 | 2.46 |
| Basic Weighted Average Shares (millions) | 4,303 | 4,309 |
| Diluted Weighted Average Shares (millions) | 4,313 | 4,320 |
| Dividends Per Share | 2.06 | 1.965 |
| Effective Tax Rate | 17.88% | 18.62% |

---

## BALANCE SHEET TAB

Source: Consolidated Balance Sheets  
⚠️ Enter **both columns**: FY2025 = current year | FY2024 = prior year (`startYear_*`)

### ASSETS

| Line Item | FY2025 (Dec 31) | FY2024 (Dec 31) |
|-----------|----------------:|----------------:|
| **CURRENT ASSETS** | | |
| Cash & Cash Equivalents | 10,270 | 10,828 |
| Short-term Investments | 5,536 | 3,743 |
| *Cash, Cash Equiv. & Short-term Investments (total)* | *15,806* | *14,571* |
| Total Receivables, Net | 3,038 | 3,569 |
| Inventories | 4,425 | 4,728 |
| Prepaid Expenses & Other Current Assets | 2,433 | 2,998 |
| Other Current Assets | 5,342 | 131 |
| **Total Current Assets** | **31,044** | **25,997** |
| | | |
| **NON-CURRENT ASSETS** | | |
| Property, Plant & Equipment — Gross | 20,429 | 21,055 |
| Accumulated Depreciation | (9,119) | (9,570) |
| **PP&E — Net** | **11,310** | **11,485** |
| Goodwill | 15,491 | 18,139 |
| Other Intangible Assets, Net | 12,531 | 13,301 |
| Long-term / Equity Method Investments | 20,235 | 18,087 |
| Other Long-term Assets | 14,205 | 13,540 |
| **Total Assets** | **104,816** | **100,549** |

### LIABILITIES

| Line Item | FY2025 (Dec 31) | FY2024 (Dec 31) |
|-----------|----------------:|----------------:|
| **CURRENT LIABILITIES** | | |
| Accounts Payable | 5,649 | 5,468 |
| Accrued Expenses | 9,164 | 16,244 |
| Current Portion of Long-term Debt | 1,822 | 648 |
| Notes Payable / Short-term Debt | 1,551 | 1,499 |
| Other Current Liabilities | 3,095 | 1,390 |
| **Total Current Liabilities** | **21,281** | **25,249** |
| | | |
| **NON-CURRENT LIABILITIES** | | |
| Long-term Debt | 42,119 | 42,375 |
| Deferred Income Tax Liabilities | 2,406 | 2,469 |
| Other Long-term Liabilities | 4,735 | 4,084 |
| Minority / Noncontrolling Interest | 2,106 | 1,516 |
| **Total Liabilities** | **72,647** | **75,693** |

### EQUITY

| Line Item | FY2025 (Dec 31) | FY2024 (Dec 31) |
|-----------|----------------:|----------------:|
| Common Stock | 1,760 | 1,760 |
| Additional Paid-in Capital (APIC) | 20,581 | 19,801 |
| Retained Earnings — **POSITIVE** | 80,382 | 76,054 |
| Treasury Stock — enter as **NEGATIVE** | (56,423) | (55,916) |
| Accumulated Other Comprehensive Income (Loss) | (14,105) | (16,779) |
| **Total Equity** | **32,169** | **24,856** |
| | | |
| **Total Liabilities & Shareholders’ Equity** | **104,816** | **100,549** |
| Total Common Shares Outstanding (millions) | 4,302 | 4,302 |

**Balance check:**
- FY2025: $104,816 = $72,647 + $32,169 ✅
- FY2024: $100,549 = $75,693 + $24,856 ✅

---

## CASH FLOW TAB

Source: Consolidated Statements of Cash Flows

| Line Item | FY2025 | FY2024 |
|-----------|-------:|-------:|
| **OPERATING ACTIVITIES** | | |
| Net Income (consolidated) | 13,137 | 10,649 |
| Changes in Working Capital | (7,208) | (6,234) |
| **Net Cash from Operating Activities (CFO)** | **7,408** | **6,805** |
| | | |
| **INVESTING ACTIVITIES** | | |
| Capital Expenditures — enter as **NEGATIVE** | (2,112) | (2,064) |
| Investment Purchases / (Sales), Net | 330 | 235 |
| Sale of Fixed Assets | 13 | 40 |
| Acquisition of Business | (461) | (315) |
| Sale / Maturity of Investments | 4,665 | 6,589 |
| Other Investing Cash Flow | 2,045 | 4,588 |
| **Net Cash from Investing Activities (CFI)** | **(67)** | **2,524** |
| | | |
| **FINANCING ACTIVITIES** | | |
| Issuance / (Retirement) of Debt, Net | 13 | 2,528 |
| Issuance / (Retirement) of Stock, Net | (433) | (1,048) |
| Total Cash Dividends Paid — enter as **NEGATIVE** | (8,779) | (8,359) |
| **Net Cash from Financing Activities (CFF)** | **(8,140)** | **(6,910)** |
| | | |
| Foreign Exchange Effects on Cash | 321 | (623) |
| **Net Change in Cash** | **(478)** | **1,796** |
| Beginning Cash Balance | 11,488 | 9,692 |
| Ending Cash Balance | 11,010 | 11,488 |

---

## MARKET & ASSUMPTIONS INPUTS

| Input | FY2025 | FY2024 | Source |
|-------|-------:|-------:|--------|
| KO Share Price (Dec 31) | ~$71.00 | ~$62.00 | Yahoo Finance |
| Diluted Shares Outstanding (millions) | 4,313 | 4,320 | 10-K EPS note |
| Effective Tax Rate | 17.88% | 18.62% | Income Tax footnote, 10-K |
| EBITDA (USD M) | 16,026 | 12,121 | Mergent Ratio section |
| Free Cash Flow (USD M) | 5,296 | 4,741 | Mergent Ratio section |

> ⚠️ Verify share prices with Yahoo Finance for exact Dec 31 closing prices

---

## PRE-UPLOAD SELF-CHECK

- [ ] **Balance Sheet balances both years:** $104,816M (FY2025) and $100,549M (FY2024)
- [ ] **No formula errors** on Ratios tab (`#REF!`, `#DIV/0!`, `#NAME?`)
- [ ] **Prior year column** (`startYear_*`) fully populated with FY2024 figures
- [ ] **Treasury stock** entered as negative in both years
- [ ] **AOCI** entered as negative in both years
- [ ] **Capex** entered as negative
- [ ] **Dividends paid** entered as negative
- [ ] **Cover tab** completed: U.S. GAAP, USD millions, FYE Dec 31, FY2025 current / FY2024 prior
- [ ] File saved as: `models/builds/2026-05-10-coca-cola-financials.xlsx`
- [ ] Commit message: `Populate Coca-Cola FY2025 + FY2024 financials from Mergent source`

---

## RATIO BENCHMARKS (Mergent — verify against your Ratios tab)

| Ratio | FY2025 | FY2024 |
|-------|-------:|-------:|
| Gross Margin | 61.6% | 61.1% |
| Operating Margin | 30.0% | 24.9% |
| Net Profit Margin | 27.3% | 22.6% |
| EBITDA Margin | 32.2% | 27.2% |
| Current Ratio | 1.46 | 1.03 |
| Quick Ratio | 1.25 | 0.84 |
| Total Debt / Total Equity | 135.8% | 176.5% |
| LT Debt / Capital | 55.1% | 61.6% |
| Asset Turnover | 0.457 | 0.468 |
| Days Inventory (DOH) | 88 | 94 |
| Days Payable (DPO) | 112 | 109 |
| Free Cash Flow (USD M) | 5,296 | 4,741 |
| Return on Equity (normalized) | 45.9% | 38.8% |
| Return on Assets (normalized) | 13.0% | 9.9% |
