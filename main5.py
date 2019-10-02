import streamlit as st
import numpy as np
import time

# Get some data.
data = np.random.randn(10, 2)

st.sidebar.title("parameters")
st.sidebar.button("push")
st.sidebar.plotly_chart()

# Show the data as a chart.
chart = st.line_chart(data)
#while True:
# Wait 1 second, so the change is clearer.
time.sleep(1)

# Grab some more data.
data2 = np.random.randn(10, 2)

# Append the new data to the existing chart.
chart.add_rows(data2)