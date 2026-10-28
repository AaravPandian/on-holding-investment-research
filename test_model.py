import math

import pytest

from src.model import (all_forecasts, all_valuations, economic_shares_m,
                       exit_value, historical_analysis, load_assumptions)


def test_hist_sales_2025():
    h = historical_analysis().set_index("year")
    assert h.at[2025, "revenue_chf_m"] == pytest.approx(3014.0)


def test_hist_yoy_growth_2025():
    h = historical_analysis().set_index("year")
    assert h.at[2025, "revenue_growth"] == pytest.approx(3014 / 2318.3 - 1)


def test_dtc_ratio_2025():
    h = historical_analysis().set_index("year")
    assert h.at[2025, "dtc_mix"] == pytest.approx(1260.5 / 3014)


def test_apac_growth_2025():
    h = historical_analysis().set_index("year")
    assert h.at[2025, "apac_revenue_chf_m"] / h.at[2024, "apac_revenue_chf_m"] - 1 > .9


def test_price_snapshot_and_fx():
    a = load_assumptions()
    assert a["market_price_usd"] == 35.41
    assert a["usd_chf"] == .827


def test_economic_share_class_adjustment():
    a = load_assumptions()
    assert 335 < economic_shares_m(a) < 337


def test_base_revenue_monotone():
    f = all_forecasts()
    b = f[f["scenario"] == "Base"]
    assert b["revenue_chf_m"].is_monotonic_increasing


def test_all_scenarios_11_rows():
    f = all_forecasts()
    assert len(f) == 33
    assert set(f["scenario"]) == {"Bear", "Base", "Bull"}


def test_terminal_year_order():
    v = all_valuations()
    t = v[v["year"] == 2031].set_index("scenario")
    assert t.at["Bear", "discounted_price_usd"] < t.at["Base", "discounted_price_usd"] < t.at["Bull", "discounted_price_usd"]


def test_valuation_manual_formula():
    a = load_assumptions()
    v = exit_value(a, "Base", 2031)
    expected = (v["revenue_chf_m"] * 3 / economic_shares_m(a) /
                a["usd_chf"] / (1+a["required_equity_return"])**5)
    assert v["discounted_price_usd"] == pytest.approx(expected)


def test_10_year_exit():
    a = load_assumptions()
    v = exit_value(a, "Base", 2036)
    assert v["revenue_chf_m"] > 10000
    assert math.isfinite(v["discounted_price_usd"])


def test_only_years_2031_2036():
    with pytest.raises(ValueError):
        exit_value(load_assumptions(), "Base", 2030)
