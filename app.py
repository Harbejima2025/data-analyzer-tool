import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Data Analysis & Sharing Tool")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data", df)

    if st.checkbox("Show summary"):
        st.write(df.describe())

    chart_type = st.selectbox("Choose chart type", ["Bar", "Line", "Scatter"])
    x_axis = st.selectbox("X-axis", df.columns)
    y_axis = st.selectbox("Y-axis", df.columns)

    if chart_type == "Bar":
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif chart_type == "Line":
        fig = px.line(df, x=x_axis, y=y_axis)
    else:
        fig = px.scatter(df, x=x_axis, y=y_axis)

    st.plotly_chart(fig)

    st.download_button("Download Data as CSV", df.to_csv(index=False), "processed_data.csv", "text/csv")
