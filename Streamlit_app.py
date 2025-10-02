import streamlit as st

from modules.oranges import plot_orange

st.title("Orange Plot Example")

if st.button("Show Plot"):
    plot_orange()

st.write('hello world')
