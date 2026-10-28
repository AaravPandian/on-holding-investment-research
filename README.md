# On Holding (NYSE: ONON) — Company Valuation & Long-Term Investment Research

**Beginner finance + data portfolio project | Excel · Python · Pandas · SQLite · Investment Research · optional Streamlit/Plotly**

> **Research question:** Can On Holding's premium sportswear positioning, direct-to-consumer (DTC) strategy and international expansion make it a much larger company by 2031–2036, and what might that growth be worth to equity holders?
>
> **As-of:** Financial statements: Q2 / H1 2026 (released 11 Aug 2026); FY2025 annual report; market-price and USD/CHF reference: **19 Oct 2026**. No live prices. All analyst forecasts are **illustrative**, not management guidance, and are **not investment advice**.

## Results at a glance

| Metric | Historical reported figure |
|:--|--:|
| FY2025 sales (CHF m) | 3,014.0 |
| FY2025 revenue growth | 30.0% |
| FY2025 gross margin | 62.8% |
| FY2025 adjusted EBITDA margin | 18.8% |
| FY2025 DTC share | 41.8% |
| Q2 2026 sales (CHF m) | 850.3 |
| Q2 2026 growth, reported / constant-currency | 13.5% / 21.6% |
| Q2 2026 DTC sales growth, reported | 26.0% |
| Q2 2026 APAC sales growth, reported | 43.1% |
| Q2 2026 Americas sales growth, reported | 4.5% |

**Research conclusion (illustrative, not advice): WATCHLIST / HOLD at the October 19, 2026 USD 35.41 reference.** On's growth and DTC trajectory are impressive, but underwriting a decade of premium multiple preservation is demanding. The base scenario models approximately **CHF 7.37bn in 2031 revenue and CHF 11.34bn in 2036**. A discounted price-to-sales exit methodology yields roughly **USD 47.22 for the 2031 exit and USD 35.91 for the 2036 exit in end-2026-equivalent dollars**, compared to USD 35.41 market reference. These are conditional scenario outputs, **not predictions or traditional analyst target prices**. Read the [research report](docs/investment_research.md) before drawing any conclusions.

### Download and explore

| Path | Purpose |
|:--|:--|
| `excel/ONON_Valuation_Model.xlsx` | Editable Excel financial model, assumptions, growth forecasts, valuation, sensitivities and source URLs |
| `docs/investment_research.md` | Structured investment research note: thesis, evidence, risks, valuation and recommendation |
| `docs/beginner_learning_guide.md` | Learn to explain the project step by step |
| `data/historical_financials.csv` | 2023–2025 audited financial metrics (CHF millions) |
| `data/q2_2026_snapshot.csv` | Q2 2026 operating update and comparison |
| `data/model_assumptions.json` | EDIT HERE to rerun Python scenarios (separate from Excel editable assumptions) |
| `src/model.py` | Read sources, calculate KPIs, build 2026E–2036 revenue and share-price scenarios |
| `src/build_analysis.py` | Create output CSVs, a SQLite database and an offline Plotly chart |
| `app.py` | Optional interactive Streamlit dashboard |
| `sql/questions.sql` | Six beginner SQL questions and working queries |
| `tests/test_model.py` | Automated sanity checks |
| `data/sources.csv` | Links, dates and uses of every underlying source |

## Setup and run on a Mac

```bash
# 1. Open Terminal in the extracted project folder.
python3 -m venv .venv
source .venv/bin/activate

# 2. Install tools
python -m pip install -r requirements.txt

# 3. Recreate forecasts, valuations, a local SQLite database, and a Plotly HTML chart
python -m src.build_analysis

# 4. Run tests
python -m pytest -q

# 5. Optional dashboard
python -m streamlit run app.py
```

The project includes **pre-generated output files**, so you can read the research, open the Excel model and inspect the CSVs **without installing Python**. Internet access is not required to run the dashboard after dependencies are installed; its data is bundled.

## Methodology: two transparent steps

1. **Business forecast:** Start from FY2026 revenue at CHF 3.515bn, the midpoint of the company's Q2 2026 full-year *reported CHF revenue guidance* of CHF 3.47–3.56bn. Apply each scenario's explicit annual sales-growth assumptions from 2027 to 2036. Estimate long-run adjusted EBITDA to illustrate operating leverage; these margins are **not forward company guidance**.
2. **Equity valuation cross-check:** Apply an *assumed* price-to-sales (P/S) multiple to forecast CHF revenues in 2031 or 2036. Convert the equity valuation to Class A economic-equivalent per-share value (Class A + one-tenth of Class B + disclosed dilutive awards), convert from CHF to USD using a **constant assumed USD/CHF rate of 0.8270**, and discount 5 or 10 years back to an approximate end-2026 equivalent using an **11% required annual equity return**. Compare with ONON's historical October 19, 2026 close of USD 35.41.

A P/S multiple is not an enterprise value multiple. **Do not add net cash to a P/S equity valuation**. This exercise deliberately avoids a full DCF, transaction costs, dividend forecasts, changing share counts, FX forecasts, future lease effects, capital allocation or trading execution. These exclusions are important limitations, not hidden assumptions. The end-2026 discount anchor is an approximation; the equity price reference is dated 19 Oct, not 31 Dec.

## Assumptions vs facts

- **Reported:** FY2023–25 statements, Q2 2026 metrics, June 2026 share counts, company FY2026 guidance. Values in CHF millions unless stated.
- **Market reference:** USD 35.41 ONON price and 0.8270 CHF per USD, both dated 19 Oct 2026. Never mistake the reference for a live quote.
- **Author's scenarios:** all 2027–36 sales growth, terminal P/S, equity discount rate, long-run adjusted EBITDA margins, USD/CHF held constant. All can be edited. The forecasts are hypotheses—not company guidance or consensus estimates.

## Why Class B share treatment matters

On reports Class A and Class B ordinary shares with different economic rights. The company's filing specifies a conversion of **ten Class B shares into one Class A share**. The model uses 301.715535m Class A and 324.991680m Class B outstanding as of 30 Jun 2026 and a separately shown approximation for awards with dilutive effects. It therefore uses about **336.109m** Class A economic-equivalent shares. It must **not** simply add 301.7m and 325.0m as though these were equally economic.

## Sources and attribution

1. [On Holding AG 2025 Form 20-F — SEC](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm)
2. [On Q2 2026 earnings release — SEC](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)
3. [On interim financial statements, June 2026 — SEC](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/onholdingag-20260630_d2.htm)
4. [ONON historical stock prices — YCharts](https://ycharts.com/companies/ONON/price)
5. [USD/CHF October 19 rate — Investing.com](https://www.investing.com/currencies/usd-chf-historical-data)

Historical totals occasionally differ by CHF 0.1m due to management's rounding. Third-party price/FX data may be delayed or corrected. Refer to the original source when refreshing. All charts and analysis are independently generated from the bundled data; company graphics and report PDFs are not redistributed.

## How to use this project in an application

**Example project description:** “Researched On Holding (NYSE: ONON) using audited annual statements and its Q2 2026 disclosure; analysed DTC mix, regional revenue and profitability with Python/Pandas; built an editable 2026E–2036 Excel model and bear/base/bull P/S valuation with transparent share-class/FX assumptions; produced a sourced investment research note and SQL analyses.”

Only claim that you personally understand, improved, or independently validated the work after studying it. Start with `docs/beginner_learning_guide.md`.

## Limitations / disclosure

Educational research only; no investment or trading recommendation, no guarantee or audited independent financial advice. A high-growth company can be a poor investment if purchased at a high multiple. This model is unusually sensitive to terminal P/S, currency translation and assumed discount rate; verify current company filings and prices before reusing it.
