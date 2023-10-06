import streamlit as st
import pandas as pd
import plotly.express as px

# Read the csv file into a pandas DataFrame
df = pd.read_csv('dataset.csv')

# Added a header with text
st.header("Car Advertisement Dashboard")

# Create a histogram using Plotly Express
fig = px.histogram(df, x="price")
st.plotly_chart(fig)

# Create a scatter plot using Plotly Express
fig = px.scatter(df, x="model_year", y="odometer", color="condition")
st.plotly_chart(fig)

show_histogram = st.checkbox("Show Histogram")
if show_histogram:
        fig = px.histogram(df, x="condition")
        st.plotly_chart(fig)
        
