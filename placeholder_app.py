import json
import requests
import streamlit as st
import time


data = []
counter = 0

if data is None:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    json_data = response.json()
    with open("placeholder_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
else:
    with open("placeholder_data.json", "r") as read_file:
        data = json.load(read_file)

## Draw streamlit app
st.title("Placeholder data")
st.text("The section below holds placeholder data. It updates ever 4 seconds and loops back to the initial element after 4 iterations.")

## Container holding multiple elements
placeholder = st.empty()

while True:
    with placeholder.container():
        ## Json data
        st.json(data[counter])

        st.divider()

        ## individual elements
        st.subheader("User ID")
        st.text(data[counter]["userId"])
        st.subheader("ID")
        st.text(data[counter]["id"])
        st.subheader("Title")
        st.text(data[counter]["title"])
        st.subheader("Body")
        st.text(data[counter]["body"])

        ## sleep timer
        time.sleep(5)
        counter+=1
        if counter > 3:
            counter = 0
