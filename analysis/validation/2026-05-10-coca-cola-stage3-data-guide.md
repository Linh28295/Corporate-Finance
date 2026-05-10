# Stage 3 Data Entry Guide
## The Coca-Cola Company (KO) — FY2024 + FY2023

**Template file:** `models/templates/performance-ratios-template.xlsx`  
**Save populated build as:** `models/builds/2026-05-10-coca-cola-financials.xlsx`  
**Source:** KO 10-K FY2024 (filed February 2025) via SEC EDGAR — [edgar.sec.gov](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=KO&type=10-K)  
**Units:** USD millions (all figures in millions unless stated)  
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
| Current Year | FY2024 (Jan 1 – Dec 31, 2024) |
| Prior Year | FY2023 (Jan 1 – Dec 31, 2023) |
| Source 10-K URL | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=KO&type=10-K |
| Analyst | Nguyen Bui Ngoc Linh |
| Date Populated | 2026-05-10 |
| IFRS / GAAP Notes | U.S. GAAP. Revenue reported net of excise taxes. Equity method investments material (∼$17B) — included in non-current assets. Retained earnings (reinvested earnings) are negative due to cumulative buybacks exceeding cumulative net income. |

---

## Step 1 — Income Statement Tab (`INC_*` named ranges)

Source: **Consolidated Statements of Income** in the 10-K

| Named Range (approximate) | 10-K Line Item | FY2024 col | FY2023 col |
|--------------------------|----------------|-----------|----------|
| `INC_Revenue` | Net operating revenues | From 10-K | From 10-K |
| `INC_COGS` | Cost of goods sold | From 10-K | From 10-K |
| `INC_GrossProfit` | Gross profit | From 10-K | From 10-K |
| `INC_SGA` | Selling, general and administrative expenses | From 10-K | From 10-K |
| `INC_OtherOperating` | Other operating charges | From 10-K | From 10-K |
| `INC_OperatingIncome` | Operating income | From 10-K | From 10-K |
| `INC_InterestExpense` | Interest expense | From 10-K | From 10-K |
| `INC_InterestIncome` | Interest income | From 10-K | From 10-K |
| `INC_EquityIncome` | Equity income (net) | From 10-K | From 10-K |
| `INC_EBT` | Income before income taxes | From 10-K | From 10-K |
| `INC_TaxExpense` | Income taxes | From 10-K | From 10-K |
| `INC_NetIncome` | Net income attributable to shareowners of KO | From 10-K | From 10-K |
| `INC_SharesDiluted` | Weighted avg diluted shares outstanding | From 10-K | From 10-K |
| `INC_EPSDiluted` | Diluted net income per share | From 10-K | From 10-K |

**Tips for KO specifically:**
- Use *Net income attributable to shareowners of The Coca-Cola Company* (not total consolidated net income which includes noncontrolling interests)
- Interest expense is a **positive** number in the template even though it reduces income
- Equity income from bottling investments is material — do not omit it

---

## Step 2 — Balance Sheet Tab (`BAL_*` and `startYear_*` named ranges)

Source: **Consolidated Balance Sheets** in the 10-K  
⚠️ Fill **both** current year (Dec 31, 2024) AND prior year (Dec 31, 2023) columns. Prior year = `startYear_*` ranges.

### Current Assets
| Named Range | 10-K Line Item |
|------------|----------------|
| `BAL_Cash` | Cash and cash equivalents |
| `BAL_ShortTermInvestments` | Short-term investments / Marketable securities |
| `BAL_AccountsReceivable` | Trade accounts receivable, net |
| `BAL_Inventories` | Inventories |
| `BAL_PrepaidOther` | Prepaid expenses and other current assets |
| `BAL_TotalCurrentAssets` | Total current assets |

### Non-Current Assets
| Named Range | 10-K Line Item |
|------------|----------------|
| `BAL_EquityInvestments` | Equity method investments (this is large for KO — ~$17B) |
| `BAL_PPE_Net` | Property, plant and equipment — net |
| `BAL_Goodwill` | Goodwill |
| `BAL_OtherIntangibles` | Other intangible assets |
| `BAL_OtherNonCurrent` | Other non-current assets |
| `BAL_TotalAssets` | Total assets |

### Current Liabilities
| Named Range | 10-K Line Item |
|------------|----------------|
| `BAL_AccountsPayable` | Accounts payable and accrued expenses |
| `BAL_CurrentDebt` | Current maturities of long-term debt |
| `BAL_OtherCurrentLiabilities` | Other current liabilities |
| `BAL_TotalCurrentLiabilities` | Total current liabilities |

### Non-Current Liabilities
| Named Range | 10-K Line Item |
|------------|----------------|
| `BAL_LongTermDebt` | Long-term debt |
| `BAL_DeferredTax` | Deferred income tax liabilities |
| `BAL_OtherNonCurrentLiabilities` | Other non-current liabilities |
| `BAL_TotalLiabilities` | Total liabilities |

### Equity
| Named Range | 10-K Line Item |
|------------|----------------|
| `BAL_CommonStock` | Common stock |
| `BAL_APIC` | Capital surplus |
| `BAL_RetainedEarnings` | Reinvested earnings — **this will be NEGATIVE** for KO |
| `BAL_AOCI` | Accumulated other comprehensive income (loss) |
| `BAL_TreasuryStock` | Treasury stock — enter as **NEGATIVE** |
| `BAL_TotalEquity` | Equity attributable to shareowners of KO |
| `BAL_TotalLiabilitiesAndEquity` | Total liabilities and equity |

**Key check:** `BAL_TotalAssets` = `BAL_TotalLiabilitiesAndEquity` for both years.

---

## Step 3 — Cash Flow Tab (`CASH_*` named ranges)

Source: **Consolidated Statements of Cash Flows** in the 10-K

### Operating Activities
| Named Range | 10-K Line Item |
|------------|----------------|
| `CASH_NetIncome` | Net income (consolidated, before noncontrolling interests) |
| `CASH_DA` | Depreciation and amortization |
| `CASH_StockComp` | Stock-based compensation expense |
| `CASH_WorkingCapital` | Net change in operating assets and liabilities |
| `CASH_OtherOperating` | Other operating activities (net) |
| `CASH_CFO` | Net cash provided by operating activities |

### Investing Activities
| Named Range | 10-K Line Item |
|------------|----------------|
| `CASH_Capex` | Purchases of property, plant and equipment — enter as **NEGATIVE** |
| `CASH_Acquisitions` | Acquisitions of businesses (net of cash) |
| `CASH_InvestmentPurchases` | Purchases of investments |
| `CASH_InvestmentProceeds` | Proceeds from disposals of investments |
| `CASH_CFI` | Net cash used in investing activities |

### Financing Activities
| Named Range | 10-K Line Item |
|------------|----------------|
| `CASH_DebtIssuance` | Issuances of debt |
| `CASH_DebtRepayment` | Payments of debt — enter as **NEGATIVE** |
| `CASH_DividendsPaid` | Dividends paid — enter as **NEGATIVE** |
| `CASH_Buybacks` | Purchases of treasury stock — enter as **NEGATIVE** |
| `CASH_CFF` | Net cash used in financing activities |
| `CASH_NetCashChange` | Net increase (decrease) in cash during period |

---

## Step 4 — Market & Assumptions

| Input | Where to find it | Notes |
|-------|-----------------|-------|
| Share price (FY2024 year-end) | KO closing price Dec 31, 2024 (Yahoo Finance) | For P/E and market cap ratios |
| Share price (FY2023 year-end) | KO closing price Dec 31, 2023 | Prior year market ratios |
| Diluted shares outstanding | 10-K — EPS footnote or IS | Use weighted average diluted |
| Income tax rate | 10-K — Income Tax footnote | KO effective rate ~18–19% |
| Cost of equity / WACC | Use CAPM or instructor-provided rate | Beta for KO ∼ 0.55–0.60 (defensive stock) |

---

## Self-Check Before Uploading

- [ ] Balance Sheet balances both years: Total Assets = Total Liabilities + Equity
- [ ] No `#REF!`, `#DIV/0!`, or `#NAME?` errors on Ratios tab
- [ ] Prior year (`startYear_*`) cells populated — otherwise start-of-year ROA/ROE will fail
- [ ] Treasury stock and reinvested earnings entered as negatives
- [ ] All figures in consistent units (millions throughout)
- [ ] Cover tab completed with source URL, standard, currency, FYE
