"""Run via: python -m src.build_analysis"""
from pathlib import Path
import sqlite3

import pandas as pd

from .model import ROOT, all_forecasts, all_valuations, historical_analysis


def build(output_dir: Path | None = None):
    output_dir = output_dir or ROOT / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)
    historical = historical_analysis()
    forecasts = all_forecasts()
    values = all_valuations()
    historical.to_csv(output_dir / "historical_metrics.csv", index=False)
    forecasts.to_csv(output_dir / "forecast_2026_2036.csv", index=False)
    values.to_csv(output_dir / "valuation_scenarios.csv", index=False)
    with sqlite3.connect(output_dir / "on_holding.db") as db:
        historical.to_sql("historical_financials", db, if_exists="replace", index=False)
        forecasts.to_sql("scenario_forecasts", db, if_exists="replace", index=False)
        values.to_sql("scenario_valuations", db, if_exists="replace", index=False)
    try:
        import plotly.express as px
        fig = px.line(forecasts, x="year", y="revenue_chf_m", color="scenario", markers=True,
                      title="On Holding: illustrative 2026E–2036 revenue paths")
        fig.update_layout(yaxis_title="Revenue (CHF millions)", xaxis_title="Fiscal year")
        fig.write_html(output_dir / "revenue_scenarios.html", include_plotlyjs=True)
    except ImportError:
        print("Plotly not installed: skipped HTML chart")
    print("Generated metrics, forecasts, valuations and SQLite database:", output_dir)
    print(values[["scenario", "year", "discounted_price_usd", "upside_downside_pct"]].to_string(index=False))


if __name__ == "__main__":
    build()
