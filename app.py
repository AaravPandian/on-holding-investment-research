"""Streamlit bonus dashboard (optional for the beginner project)."""
import copy

import pandas as pd
import plotly.express as px
import streamlit as st

from src.model import (all_forecasts, all_valuations, historical_analysis,
                       load_assumptions, economic_shares_m)

st.set_page_config(page_title="ONON Investment Research", page_icon="📈", layout="wide")
st.title("On Holding | Long-term investment research")
st.caption("Educational analysis • Source data through Q2 2026 • Price reference: 19 Oct 2026 • Not investment advice")
st.info("Forecasts, 2031/2036 P/S multiples and the discount rate below are **analyst scenarios**, not On guidance.")

inputs = copy.deepcopy(load_assumptions())
with st.sidebar:
    st.header("Edit assumptions")
    inputs["required_equity_return"] = st.slider("Required annual equity return", .05, .20,
                                                 inputs["required_equity_return"], .005, format="%.1f")
    inputs["market_price_usd"] = st.number_input("Reference ONON share price (USD)",
                                                min_value=0.1, value=float(inputs["market_price_usd"]))
    inputs["usd_chf"] = st.number_input("USD/CHF (CHF for 1 USD)",
                                      min_value=0.1, value=float(inputs["usd_chf"]), step=.001, format="%.4f")
    st.divider()
    st.caption("Modify the 2031/2036 exit price-to-sales assumptions")
    for name in ("Bear", "Base", "Bull"):
        with st.expander(name):
            for yr in (2031, 2036):
                key = f"exit_ps_{yr}"
                inputs["scenarios"][name][key] = st.number_input(
                    f"{name} {yr} exit P/S", min_value=.1,
                    value=float(inputs["scenarios"][name][key]), step=.1,
                    key=f"{name}_{yr}")

hist = historical_analysis()
forecasts = all_forecasts(inputs)
val = all_valuations(inputs)
a, b, c, d = st.columns(4)
a.metric("2025 net sales", "CHF 3.014bn")
b.metric("2025 DTC revenue mix", f"{hist.iloc[-1]['dtc_mix']:.1%}")
c.metric("Q2 2026 CC revenue growth", "21.6%")
d.metric("Economic Class A shares", f"{economic_shares_m(inputs):.1f}m")

tab1, tab2, tab3 = st.tabs(["Historical performance", "Growth scenarios", "Valuation"])
with tab1:
    st.plotly_chart(px.bar(hist, x="year", y=["dtc_revenue_chf_m", "wholesale_revenue_chf_m"],
                           barmode="stack", title="Revenue by route to market (CHF m)",
                           labels={"value": "Sales (CHF m)", "variable":"Channel"}), use_container_width=True)
    st.plotly_chart(px.line(hist, x="year", y=["gross_margin","adj_ebitda_margin"],
                            title="Margins (decimal scale)", markers=True), use_container_width=True)
    st.dataframe(hist.round(3), hide_index=True)
with tab2:
    st.plotly_chart(px.line(forecasts, x="year", y="revenue_chf_m", color="scenario", markers=True,
                            title="How large could On become by 2031–2036?",
                            labels={"revenue_chf_m":"Sales (CHF m)"}), use_container_width=True)
    st.dataframe(forecasts.round(3), hide_index=True)
with tab3:
    st.plotly_chart(px.bar(val, x="scenario", y="discounted_price_usd", color="year", barmode="group",
                           title="Illustrative present-equivalent USD share prices"), use_container_width=True)
    st.dataframe(val.round(2), hide_index=True)
    st.caption("Method: forecast CHF sales × assumed equity P/S ÷ economic Class A-equivalent shares ÷ USD/CHF; discount from end of exit year to end-2026. Does not model dilution, dividends or future FX changes.")
    st.download_button("Download scenario valuations CSV", val.to_csv(index=False), "onon_valuations.csv")
