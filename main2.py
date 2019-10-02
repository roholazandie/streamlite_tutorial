import streamlit as st
x = st.slider('x', 0, 200, 5)
st.write(x, 'squared is', x * x)

if st.button("this"):
    st.write("this is this")
else:
    st.write("No it doesnt work")

agree = st.checkbox("I agree")

if agree:
    st.write("you agree")

genre = st.radio('Whats your favorite movie genre', ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('you like comedy')
elif genre == 'Drama':
    st.write("you like Drama")
elif genre == 'Documentary':
    st.write("you like documentray")
else:
    st.write("you're tasteless")