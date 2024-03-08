import streamlit as st
import pandas as pd
import numpy as np

st.write(
        """
This is an app for some Movie titles!
        """
        )

st.sidebar.header("User data")
st.sidebar.markdown("""
    [CSV input file]
                    """)

file  = st.sidebar.file_uploader("Upload csv", type=["csv"])