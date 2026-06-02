import streamlit as st
import pandas as pd

from src.analytics.funnel import funnel_conversion
from src.analytics.unit_economics import unit_economics

st.set_page_config(page_title="AI RevOps Auditor", layout="wide")

st.title("📊 AI RevOps Auditor")

# =========================
# UPLOAD CSV
# =========================
uploaded_file = st.file_uploader("Upload funnel CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df)

    # =========================
    # FUNNEL
    # =========================
    st.subheader("Funnel Analysis")

    funnel = funnel_conversion(df)
    st.json(funnel)

    # =========================
    # UNIT ECONOMICS (mock inputs)
    # =========================
    st.subheader("Unit Economics")

    economics = unit_economics(
        marketing_cost=10000,
        new_customers=50,
        avg_revenue=1200,
        lifetime_months=12,
        monthly_revenue=100
    )

    st.json(economics)

    # =========================
    # EXECUTIVE INSIGHTS
    # =========================
    st.subheader("Executive Insights")

    st.write("⚠️ Funnel leakage detected between stages (demo logic)")
    st.write("💰 CAC vs LTV ratio indicates growth efficiency")
    st.write("📉 Payback period suggests scaling opportunity")
else:
    st.info("Upload a CSV to start analysis")
