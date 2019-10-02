import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy
import pandas
import time

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")

df = pandas.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write()

chart_data = pandas.DataFrame(
    numpy.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

# map_data = pandas.DataFrame(
#     numpy.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
#
# st.map(map_data)


if st.checkbox('Show dataframe'):
    chart_data = pandas.DataFrame(
        numpy.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

st.write(option)

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text('Iteration %d' % i)
    bar.progress(i + 1)
    time.sleep(0.1)

st.success("done")
