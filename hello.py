import os

from dotenv import load_dotenv
import streamlit as st
load_dotenv()


key = os.environ["SOMETHING_KEY"]

st.write("# Hello")

st.write("This is hello project!")
st.write(f"{key}")
