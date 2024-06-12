import streamlit as st
import numpy as np
import pandas as pd
#import graphviz
import plotly.figure_factory as ff
#from bokeh.plotting import figure

#st.balloons()
st.markdown("# Data Evaluation App")

st.title('web 3')

chart_data = pd.DataFrame(
     np.random.randn(6, 3),
     columns=['a', 'b', 'c'])


option = st.selectbox(
    "How would you like to be contacted?",
    ("area", "table", "line", "chart"))

st.write("You selected:", option)
if option =="area":
    st.area_chart(chart_data)

elif option =="table":
    st.table(chart_data)

elif option =="line":
    st.line_chart(chart_data)

elif option =="chart":
    st.bar_chart(chart_data)


if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")



x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label='x',
    y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

#st.bokeh_chart(p, use_container_width=True)