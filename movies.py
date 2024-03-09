import streamlit as st
import pandas as pd
import numpy as np

st.write(
        """
This is an app for some Movie titles!
        """
        )

st.sidebar.header("User data") ## Header
st.sidebar.markdown("""
    [CSV input file]
                    """) ## text-to-HTML conversion tool. Write in plain text, convert to structurally valid HTML

file  = st.sidebar.file_uploader("Upload csv", type=["csv"]) ## Browse to folder containing CSV

## Set DataFrame if file is valid
if file is not None:
        df = pd.read_csv(file)

df

st.sidebar.selectbox("Test1", ("one", "two", "three")) ## selection box
st.sidebar.slider("Some tag", 30,60,40) ## ie 40 = default value
st.sidebar.text_input("Name: ") ## text input field