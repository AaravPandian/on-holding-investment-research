-- Run against outputs/on_holding.db (created by python -m src.build_analysis)
-- 1. How quickly did On grow each year?
SELECT year, ROUND(revenue_chf_m,1) AS sales_chf_m, ROUND(revenue_growth*100,1) AS yoy_pct
FROM historical_financials ORDER BY year;

-- 2. What portion of net sales is DTC?
SELECT year, ROUND(dtc_mix*100,1) AS dtc_mix_pct
FROM historical_financials ORDER BY year;

-- 3. Has the APAC share of sales changed?
SELECT year, ROUND(apac_mix*100,1) AS apac_share_pct
FROM historical_financials ORDER BY year;

-- 4. Are adjusted EBITDA margins improving?
SELECT year, ROUND(adj_ebitda_margin*100,1) AS adj_ebitda_margin_pct
FROM historical_financials ORDER BY year;

-- 5. 2031 and 2036 outcomes by scenario
SELECT scenario, year, ROUND(revenue_chf_m,0) AS revenue_chf_m,
       ROUND(discounted_price_usd,2) AS discounted_usd_per_share
FROM scenario_valuations ORDER BY year, scenario;

-- 6. In which forecast year does base case exceed CHF 5bn?
SELECT MIN(year) AS first_above_5bn
FROM scenario_forecasts WHERE scenario='Base' AND revenue_chf_m >= 5000;
