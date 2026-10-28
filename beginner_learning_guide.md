# Beginner Learning Guide — Understand This Project Later

You can upload the completed repository now. Before speaking about it in an interview, complete the steps below and try to rebuild parts yourself.

## Week 1 — Understand the company and financial statements

- **Day 1:** Read `docs/investment_research.md`. Explain the company's products, wholesale versus DTC, and why a premium brand might earn high margins.
- **Day 2:** Open `data/historical_financials.csv` in Excel. Understand revenue, gross profit, operating profit, EBITDA, net income and cash flow.
- **Day 3:** Read On's 2025 Form 20-F (source #1 in README). Verify three numbers in our dataset yourself.
- **Day 4:** Read Q2 2026 results and explain why 13.5% *reported* growth differs from 21.6% *constant-currency* growth.
- **Day 5:** Open the Excel `History` tab. Recalculate 2025 gross margin (gross profit divided by sales).

## Week 2 — Beginner Excel modelling

- **Day 6:** Open `ONON_Valuation_Model.xlsx`. Look at blue-font / yellow-background assumptions: numbers you are allowed to change.
- **Day 7:** Open `Assumptions`, change Base 2027 growth from 20% to 15%, observe forecast revenue through 2036.
- **Day 8:** Explain compound growth using `next year's revenue = last year's revenue × (1 + growth)`.
- **Day 9:** Look at `Valuation`: explain price-to-sales, Class B economics and the CHF/USD conversion.
- **Day 10:** Change the Base 2031 multiple from 3.0× to 2.0×. Write down why the valuation falls even if revenue assumptions are unchanged.

## Week 3 — Python and Pandas

- **Day 11:** Install Python dependencies and run `python -m src.build_analysis`.
- **Day 12:** Read `src/model.py`; learn `pd.read_csv`, creating columns, `.pct_change()` and percentage margins.
- **Day 13:** Find `forward_path()`; trace Base 2027 revenue starting from FY2026E CHF 3.515bn.
- **Day 14:** Find `exit_value()`; compare the formula with Excel and calculate one share-price scenario with a calculator.
- **Day 15:** Change a `data/model_assumptions.json` growth assumption and rerun to see how the CSV forecasts change. Excel and JSON inputs are independent; changing one does not sync to the other.

## Week 4 — SQL, communication and interview

- **Day 16:** Run `python -m src.build_analysis` to create `outputs/on_holding.db`.
- **Day 17:** Execute the six queries in `sql/questions.sql` using any SQLite browser or `sqlite3` CLI.
- **Day 18:** Run `python -m pytest -q`; learn why tests protect forecasts and calculations.
- **Day 19:** Start Streamlit with `python -m streamlit run app.py` (optional). Change P/S to see sensitivity.
- **Day 20:** Record a 3-minute explanation: why On could grow, why growth alone is not a reason to buy, what would make your thesis wrong.

## Five interview questions to practice

1. Why is On's Q2 2026 reported growth lower than constant-currency growth?
2. Does growth in DTC always mean better operating profit? Explain store costs, marketing and fulfilment.
3. How can a company double revenue yet its share price still deliver a disappointing return?
4. What is the risk of assuming a long-term price-to-sales exit multiple?
5. Why is the share count not simply Class A + Class B?

## Glossary

- **DTC:** Direct-to-consumer, sales through the company's owned online stores and physical shops.
- **Gross margin:** `(revenue - cost of goods sold) / revenue`.
- **Adjusted EBITDA margin:** A company-defined non-IFRS profitability metric; not equal to free cash flow.
- **FX:** Foreign-exchange translation. On reports in CHF, while NYSE ONON is priced in USD.
- **P/S:** Price-to-sales: equity value divided by annual revenue. Unlike EV/Sales it is an equity ratio.
- **Discounting:** Divide a future amount by `(1 + required return) ^ years` to show an equivalent earlier value.
- **Scenario:** A set of what-if assumptions, not a statistical probability or a management forecast.
