import streamlit as st
import numpy as np
import time
import pandas as pd


st.empty()
my_bar = st.progress(0)
for i in range(100):
    my_bar.progress(i + 1)
    time.sleep(0.1)

st.success("done")