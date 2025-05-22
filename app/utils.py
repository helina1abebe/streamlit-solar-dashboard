# app/utils.py
import pandas as pd
import plotly.express as px

def load_data():
    # Load each CSV and tag the country
    benin = pd.read_csv("data/benin-malanville.csv")
    benin["country"] = "Benin"
    
    sierra = pd.read_csv("data/sierraleone-bumbuna.csv")
    sierra["country"] = "Sierra Leone"
    
    togo = pd.read_csv("data/togo-dapaong_qc.csv")
    togo["country"] = "Togo"
    
    # Combine all
    df = pd.concat([benin, sierra, togo], ignore_index=True)
    return df

def plot_ghi_boxplot(data, metric):
    fig = px.box(data, x="country", y=metric, color="country", title=f"{metric} Boxplot")
    return fig

def get_top_regions(data, metric, top_n=10):
    # If there's no 'region' column, fallback to 'site' or use file names
    if 'region' in data.columns:
        region_col = 'region'
    elif 'site' in data.columns:
        region_col = 'site'
    else:
        region_col = 'country'
    
    return (
       data.groupby('country', as_index=False)[metric].mean().sort_values(by=metric, ascending=False).head(10)

    )
