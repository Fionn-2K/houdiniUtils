import streamlit as st
import psutil ## PSU utilities
import time

st.title("Machine Resource App")

## Declare streamlit charts
st.write("CPU")
cpu_chart = st.line_chart()
st.write("RAM")
ram_chart = st.line_chart()

## Infinite loop
while True:
    ## Get CPU/RAM percentage
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent

    ## Add percentages to charts
    cpu_chart.add_rows([cpu_percent])
    ram_chart.add_rows([ram_percent])

    ## sleep loop for 1 second
    time.sleep(1)