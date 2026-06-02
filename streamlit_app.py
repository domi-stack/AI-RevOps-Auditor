import streamlit as st
import pandas as pd

from analytics.funnel import funnel_conversion
from analytics.unit_economics import unit_economics

st.set_page_config(page_title="AI RevOps Auditor", layout="wide")

st.title("📊 AI RevOps Auditor")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Data")
    st.dataframe(df)

    st.subheader("Funnel Analysis")
    try:
        st.json(funnel_conversion(df))
    except Exception as e:
        st.error(f"Funnel error: {e}")

    st.subheader("Unit Economics")
    try:
        st.json(unit_economics(
            10000, 50, 1200, 12, 100
        ))
    except Exception as e:
        st.error(f"Economics error: {e}")

else:
    st.info("Upload a CSV to start analysis")
