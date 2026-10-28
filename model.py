"""Simple and transparent long-horizon price-to-sales valuation model.

All figures in CHF millions unless specified. This is an educational model,
not a brokerage investment target or forecast by On Holding.
"""
from __future__ import annotations

import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def load_assumptions(path: Path | None = None) -> dict:
    file = path or ROOT / "data" / "model_assumptions.json"
    with open(file, encoding="utf-8") as handle:
        return json.load(handle)


def economic_shares_m(inputs: dict) -> float:
    """Class B gets 1/10th the economics of Class A, plus stated dilutive awards.

    Approximation: awards dated 2026-06-30 are used as a share-count buffer.
    """
    n = inputs["class_b_per_a"]
    return (inputs["class_a_shares_m"]
            + inputs["class_b_shares_m"] / n
            + inputs["dilutive_a_awards_m"]
            + inputs["dilutive_b_awards_m"] / n)


def forward_path(inputs: dict, scenario: str) -> pd.DataFrame:
    a = inputs["scenarios"][scenario]
    revenue = float(inputs["revenue_2026e_chf_m"])
    result = [{"scenario": scenario, "year": 2026, "growth": None,
               "revenue_chf_m": revenue}]
    for year, growth in zip(range(2027, 2037), a["growth_2027_2036"]):
        revenue *= 1 + growth
        result.append({"scenario": scenario, "year": year,
                       "growth": growth, "revenue_chf_m": revenue})
    return pd.DataFrame(result)


def exit_value(inputs: dict, scenario: str, year: int) -> dict:
    """Exit price in USD, discounted to approximate end-2026 equivalent.

    Enterprise value/lease/cash issues are avoided by using a price-to-sales
    equity multiple directly; the P/S multiple is an analyst assumption.
    No dividends, capital raises, or future share-count changes assumed.
    """
    if year not in (2031, 2036):
        raise ValueError("Year must be 2031 or 2036")
    assumptions = inputs["scenarios"][scenario]
    revenue = float(forward_path(inputs, scenario).set_index("year").at[year, "revenue_chf_m"])
    ps = float(assumptions[f"exit_ps_{year}"])
    eq_m = economic_shares_m(inputs)
    future_chf = revenue * ps / eq_m
    future_usd = future_chf / inputs["usd_chf"]
    pv_usd = future_usd / ((1 + inputs["required_equity_return"]) ** (year - 2026))
    ebitda_margin = assumptions[f"ebitda_margin_{year}"]
    return {
        "scenario": scenario, "year": year,
        "revenue_chf_m": revenue,
        "ebitda_margin": ebitda_margin,
        "illustrative_ebitda_chf_m": revenue * ebitda_margin,
        "exit_ps": ps,
        "future_price_usd": future_usd,
        "discounted_price_usd": pv_usd,
        "upside_downside_pct": (pv_usd / inputs["market_price_usd"] - 1) * 100,
    }


def all_forecasts(inputs: dict | None = None) -> pd.DataFrame:
    a = inputs or load_assumptions()
    return pd.concat([forward_path(a, name) for name in a["scenarios"]], ignore_index=True)


def all_valuations(inputs: dict | None = None) -> pd.DataFrame:
    a = inputs or load_assumptions()
    return pd.DataFrame([exit_value(a, scenario, year)
                         for scenario in a["scenarios"]
                         for year in (2031, 2036)])


def historical_analysis(path: Path | None = None) -> pd.DataFrame:
    csv = path or ROOT / "data" / "historical_financials.csv"
    df = pd.read_csv(csv).sort_values("year")
    df["revenue_growth"] = df["revenue_chf_m"].pct_change()
    df["gross_margin"] = df["gross_profit_chf_m"] / df["revenue_chf_m"]
    df["operating_margin"] = df["operating_profit_chf_m"] / df["revenue_chf_m"]
    df["adj_ebitda_margin"] = df["adjusted_ebitda_chf_m"] / df["revenue_chf_m"]
    df["dtc_mix"] = df["dtc_revenue_chf_m"] / df["revenue_chf_m"]
    df["apac_mix"] = df["apac_revenue_chf_m"] / df["revenue_chf_m"]
    # Simplification: this defined FCF excludes investing in intangible assets.
    df["simplified_fcf_chf_m"] = df["operating_cash_flow_chf_m"] - df["capex_ppe_chf_m"]
    return df
