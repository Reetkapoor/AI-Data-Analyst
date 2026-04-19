import streamlit as st
import plotly.express as px

def generate_chart(df,plan):

    chart = plan.get("chart_type")

    if chart == "none":
        return
    
    x= plan.get("x_axis")
    y= plan.get("y_axis")

    st.subheader("Visualizaiton")

    if chart == "bar":
        fig = px.bar(df, x=x, y=y)

    elif chart == "line":
        fig = px.line(df, x=x, y=y)

    elif chart == "scatter":
        fig = px.scatter(df, x=x, y=y)

    elif chart == "histogram":
        fig = px.histogram(df, x=x)

    else :
        return
    
    st.plotly_chart(fig, use_contaner_width = True)
    st.caption(plan.get("reason", ""))

