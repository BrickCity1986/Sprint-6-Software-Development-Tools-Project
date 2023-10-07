import streamlit as st
import pandas as pd
import plotly.express as px

# Read the csv file into a pandas DataFrame
df = pd.read_csv('dataset.csv')

show_histogram = st.sidebar.checkbox("Show Histogram")

st.title("Car Advertisement Dashboard")

# Create a subheader
st.subheader("Histogram")

# Create a histogram
hist_fig = px.histogram(data_frame=df, x="price")
st.plotly_chart(hist_fig, use_container_width=True)

# Create a scatter plot
st.subheader("Scatter Plot")
scatter_fig = px.scatter(data_frame=df, x="model_year", y="odometer", color="condition")
st.plotly_chart(scatter_fig, use_container_width=True)

# Create a checkbox in the sidebar
show_histogram = st.sidebar.checkbox("Show Histogram")
if show_histogram:
        fig = px.histogram(df, x="condition")
        st.plotly_chart(fig)
