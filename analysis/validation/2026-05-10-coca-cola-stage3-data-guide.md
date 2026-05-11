# Stage 3 Data Entry Guide
## The Coca-Cola Company (KO) — FY2025 + FY2024

**Template file:** `models/templates/performance-ratios-template.xlsx`  
**Save populated build as:** `models/builds/2026-05-10-coca-cola-financials.xlsx`  
**Source:** KO 10-K FY2025 via SEC EDGAR — [edgar.sec.gov](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=KO&type=10-K)  
**Units:** USD millions  
**Reporting standard:** U.S. GAAP  
**Fiscal year end:** December 31  

---

## Step 0 — Cover & Instructions Tab (fill this first)

| Field | Value |
|-------|-------|
| Company Name | The Coca-Cola Company |
| Ticker | KO |
| Exchange | NYSE |
| Reporting Currency | USD |
| Units | Millions |
| Reporting Standard | U.S. GAAP |
| Fiscal Year End | December 31 |
| Current Year | FY2025 (Jan 1 – Dec 31, 2025) |
| Prior Year | FY2024 (Jan 1 – Dec 31, 2024) |
| Source 10-K URL | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=KO&type=10-K |
| Analyst | Nguyen Bui Ngoc Linh |
| Date Populated | 2026-05-10 |
| GAAP Notes | U.S. GAAP. Retained earnings are POSITIVE ($80,382M FY2025). Treasury stock (-$56,423M) and AOCI (-$14,105M) are large negatives that reduce total equity. Equity method investments ($20,235M) are material non-current assets. |

---

## Step 1 — Income Statement Tab (`INC_*` named ranges)

Source: **Consolidated Statements of Income** in the 10-K  
Use the **full data reference** at `analysis/validation/2026-05-10-coca-cola-financials-data-reference.md` for exact figures.

| Named Range (approximate) | 10-K Line Item | FY2025 | FY2024 |
|--------------------------|----------------|-------:|-------:|
| `INC_Revenue` | Net operating revenues | 47,941 | 47,061 |
| `INC_COGS` | Cost of goods sold | 18,397 | 18,324 |
| `INC_GrossProfit` | Gross profit | 29,544 | 28,737 |
| `INC_SGA` | Selling, general & administrative expenses | 14,521 | 14,582 |
| `INC_OtherOperating` | Other operating expenses (incl. unusual items) | 629 | 2,455 |
| `INC_OperatingIncome` | Operating income | 14,394 | 11,700 |
| `INC_InterestNet` | Interest income/(expense), net | 1,683 | 1,417 |
| `INC_OtherNet` | Other, net | (79) | (31) |
| `INC_EBT` | Net income before taxes | 15,998 | 13,086 |
| `INC_TaxExpense` | Provision for income taxes | 2,861 | 2,437 |
| `INC_NetIncome` | Net income | 13,107 | 10,631 |
| `INC_SharesDiluted` | Diluted weighted average shares (millions) | 4,313 | 4,320 |
| `INC_EPSDiluted` | Diluted EPS | 3.04 | 2.46 |

**KO-specific notes:**
- Retained earnings are **POSITIVE** — do not enter as negative
- Interest figure is net (income minus expense); source gross split from 10-K footnotes if template requires separate rows
- Equity method income from bottling investments is material — do not omit

---

## Step 2 — Balance Sheet Tab (`BAL_*` and `startYear_*` named ranges)

Source: **Consolidated Balance Sheets** in the 10-K  
⚠️ Fill **both** current year (Dec 31, 2025) AND prior year (Dec 31, 2024). Prior year = `startYear_*` ranges.

### Current Assets
| Named Range | 10-K Line Item | FY2025 | FY2024 |
|------------|----------------|-------:|-------:|
| `BAL_Cash` | Cash and cash equivalents | 10,270 | 10,828 |
| `BAL_ShortTermInvestments` | Short-term investments | 5,536 | 3,743 |
| `BAL_AccountsReceivable` | Total receivables, net | 3,038 | 3,569 |
| `BAL_Inventories` | Inventories | 4,425 | 4,728 |
| `BAL_PrepaidOther` | Prepaid expenses & other current assets | 7,775 | 3,129 |
| `BAL_TotalCurrentAssets` | Total current assets | 31,044 | 25,997 |

### Non-Current Assets
| Named Range | 10-K Line Item | FY2025 | FY2024 |
|------------|----------------|-------:|-------:|
| `BAL_PPE_Net` | PP&E — net | 11,310 | 11,485 |
| `BAL_Goodwill` | Goodwill | 15,491 | 18,139 |
| `BAL_OtherIntangibles` | Other intangible assets, net | 12,531 | 13,301 |
| `BAL_EquityInvestments` | Long-term / equity method investments | 20,235 | 18,087 |
| `BAL_OtherNonCurrent` | Other long-term assets | 14,205 | 13,540 |
| `BAL_TotalAssets` | **Total assets** | **104,816** | **100,549** |

### Current Liabilities
| Named Range | 10-K Line Item | FY2025 | FY2024 |
|------------|----------------|-------:|-------:|
| `BAL_AccountsPayable` | Accounts payable | 5,649 | 5,468 |
| `BAL_AccruedExpenses` | Accrued expenses | 9,164 | 16,244 |
| `BAL_CurrentDebt` | Current portion of LT debt + notes payable | 3,373 | 2,147 |
| `BAL_OtherCurrentLiabilities` | Other current liabilities | 3,095 | 1,390 |
| `BAL_TotalCurrentLiabilities` | Total current liabilities | 21,281 | 25,249 |

### Non-Current Liabilities
| Named Range | 10-K Line Item | FY2025 | FY2024 |
|------------|----------------|-------:|-------:|
| `BAL_LongTermDebt` | Long-term debt | 42,119 | 42,375 |
| `BAL_DeferredTax` | Deferred income tax liabilities | 2,406 | 2,469 |
| `BAL_OtherNonCurrentLiabilities` | Other long-term liabilities | 4,735 | 4,084 |
| `BAL_MinorityInterest` | Noncontrolling interest | 2,106 | 1,516 |
| `BAL_TotalLiabilities` | **Total liabilities** | **72,647** | **75,693** |

### Equity
| Named Range | 10-K Line Item | FY2025 | FY2024 |
|------------|----------------|-------:|-------:|
| `BAL_CommonStock` | Common stock | 1,760 | 1,760 |
| `BAL_APIC` | Additional paid-in capital | 20,581 | 19,801 |
| `BAL_RetainedEarnings` | Retained earnings — **POSITIVE** | 80,382 | 76,054 |
| `BAL_TreasuryStock` | Treasury stock — **NEGATIVE** | (56,423) | (55,916) |
| `BAL_AOCI` | Accumulated other comprehensive loss — **NEGATIVE** | (14,105) | (16,779) |
| `BAL_TotalEquity` | **Total equity** | **32,169** | **24,856** |
| `BAL_TotalLiabilitiesAndEquity` | **Total liabilities & equity** | **104,816** | **100,549** |

**Balance check:** FY2025: 104,816 = 72,647 + 32,169 ✅ | FY2024: 100,549 = 75,693 + 24,856 ✅

---

## Step 3 — Cash Flow Tab (`CASH_*` named ranges)

Source: **Consolidated Statements of Cash Flows** in the 10-K

| Named Range | 10-K Line Item | FY2025 | FY2024 |
|------------|----------------|-------:|-------:|
| `CASH_NetIncome` | Net income (consolidated) | 13,137 | 10,649 |
| `CASH_WorkingCapital` | Changes in working capital | (7,208) | (6,234) |
| `CASH_CFO` | **Net cash from operating activities** | **7,408** | **6,805** |
| `CASH_Capex` | Capital expenditures — **NEGATIVE** | (2,112) | (2,064) |
| `CASH_Acquisitions` | Acquisition of business | (461) | (315) |
| `CASH_InvestmentNet` | Investment / divestiture activity, net | 5,008 | 11,212 |
| `CASH_CFI` | **Net cash from investing activities** | **(67)** | **2,524** |
| `CASH_DebtNet` | Issuance/(retirement) of debt, net | 13 | 2,528 |
| `CASH_Buybacks` | Stock repurchases — **NEGATIVE** | (433) | (1,048) |
| `CASH_DividendsPaid` | Dividends paid — **NEGATIVE** | (8,779) | (8,359) |
| `CASH_CFF` | **Net cash from financing activities** | **(8,140)** | **(6,910)** |
| `CASH_FXEffect` | Foreign exchange effect on cash | 321 | (623) |
| `CASH_NetCashChange` | **Net change in cash** | **(478)** | **1,796** |

---

## Step 4 — Market & Assumptions

| Input | FY2025 | FY2024 | Source |
|-------|-------:|-------:|--------|
| Share price (Dec 31) | ~$71.00 | ~$62.00 | Yahoo Finance |
| Diluted shares (millions) | 4,313 | 4,320 | 10-K EPS note |
| Effective tax rate | 17.88% | 18.62% | 10-K tax footnote |

---

## Self-Check Before Uploading

- [ ] Balance sheet balances both years: $104,816M (FY2025) and $100,549M (FY2024)
- [ ] No `#REF!`, `#DIV/0!`, or `#NAME?` errors on Ratios tab
- [ ] Prior year (`startYear_*`) fully populated with FY2024 figures
- [ ] Treasury stock and AOCI entered as **negatives**
- [ ] Capex and dividends entered as **negatives**
- [ ] Retained earnings entered as **positive**
- [ ] Cover tab: U.S. GAAP, USD millions, FYE Dec 31, FY2025 current / FY2024 prior
- [ ] File saved as: `models/builds/2026-05-10-coca-cola-financials.xlsx`
- [ ] Commit message: `Populate Coca-Cola FY2025 + FY2024 financials from Mergent source`
