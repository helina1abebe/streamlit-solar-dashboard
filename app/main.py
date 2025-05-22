# app/main.py
import streamlit as st
from utils import load_data, plot_ghi_boxplot, get_top_regions


st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("☀️ Cross-Country Solar Insights")

# Load Data
data = load_data()

# Sidebar Filters
countries = st.sidebar.multiselect("Select Countries", sorted(data["country"].unique()), default=data["country"].unique())
metric = st.sidebar.selectbox("Select Metric", [col for col in data.columns if data[col].dtype != "object" and col != "year"])

filtered_data = data[data["country"].isin(countries)]

# Boxplot
st.subheader(f"{metric} Distribution by Country")
st.plotly_chart(plot_ghi_boxplot(filtered_data, metric), use_container_width=True)

# Top Regions Table
st.subheader("Top Regions by Average " + metric)
st.dataframe(get_top_regions(filtered_data, metric))
