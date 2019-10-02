import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
from PIL import Image
import datetime
import time

x = st.sidebar.slider('x', 0, 200, 5)
options = st.sidebar.multiselect("choose data", ("x1", "x2", "x3"))
st.sidebar.text(options)
hist_data = []
group_labels = []
bin_sizes = []
with st.spinner('Waiting ...'):
    if "x1" in options:
        x1 = np.random.randn(x) - 2
        hist_data.append(x1)
        group_labels.append('Group 1')
        bin_sizes.append(.1)

    if "x2" in options:
        x2 = np.random.randn(x)
        hist_data.append(x2)
        group_labels.append('Group 2')
        bin_sizes.append(.25)
    if "x3" in options:
        x3 = np.random.randn(x) + 2
        hist_data.append(x3)
        group_labels.append('Group 3')
        bin_sizes.append(0.1)

    #time.sleep(0.4) #just for the heck of it

if hist_data:
    # Create distplot with custom bin_size
    fig = ff.create_distplot(
             hist_data, group_labels, bin_size=bin_sizes)
    # Plot!
    st.plotly_chart(fig)

else:
    st.write("there is nothing to show!")


if st.sidebar.button("See bolloons"):
    st.balloons()
    st.error("fuck")

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write("time is set to: "+str(t))

d = st.date_input(
    'Whens your birthday',
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

st.empty()

text_input = st.text_area("Text input:", "Here is the text goes, I really need this feature in future")
st.write("number of words: ", str(len(text_input.split(' '))))

t = st.text_input("text input: ", "write anything")
st.write(t)


st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
        'stuff 5',
     ],
})


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

image = Image.open('ss.png')
st.image(image, caption='Sunrise by the mountains', use_column_width=True)


audio_file = open('au.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')