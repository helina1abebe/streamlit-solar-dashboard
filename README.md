# ☀️ Cross-Country Solar Analysis Dashboard

An interactive Streamlit dashboard for visualizing and comparing solar energy potential across Benin, Sierra Leone, and Togo using Global Horizontal Irradiance (GHI) data.

## Features
- Load and combine solar datasets from three countries
- Explore GHI distributions via interactive boxplots
- Identify top-performing regions based on average GHI

## Dataset
- `data/benin-malanville.csv`
- `data/sierraleone-bumbuna.csv`
- `data/togo-dapaong_qc.csv`

## 🚀 How to Run

1. Create a virtual environment: python -m venv .venv
### Activate it:
On Windows: .venv\Scripts\activate
On Mac/Linux: source .venv/bin/activate
Install requirements: pip install -r requirements.txt
Run the app: streamlit run app/main.py
### Dependencies
Python 3.11
pandas
plotly
streamlit

Author
Helina Abebe Bekele
