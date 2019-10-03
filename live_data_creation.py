import streamlit as st
import numpy as np
import time

# Get some data.
data = np.random.randn(10, 2)

st.sidebar.title("parameters")

stop_button_exist = False
stop_button = False
if st.sidebar.button("start"):
    # Show the data as a chart.
    chart = st.line_chart(data)

    while True:
        # Grab some more data.
        data2 = np.random.randn(10, 2)
        # Append the new data to the existing chart.
        chart.add_rows(data2)
        time.sleep(1)

        if not stop_button_exist:
            stop_button = st.sidebar.button("stop")
            stop_button_exist = True
        if stop_button:
            break