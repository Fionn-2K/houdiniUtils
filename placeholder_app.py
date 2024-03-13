import json
import requests
import streamlit as st
import time

class PlaceHolder:
    ## cache url to json
    def __init__(self, url: str):
        self.url = url
        self.data = []
        self.counter = 0

        response = requests.get(self.url)
        json_data = response.json()
        with open("placeholder_data.json", "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        with open("placeholder_data.json", "r") as read_file:
            self.data = json.load(read_file)

    def createFrontEnd(self):
        ## Draw streamlit app
        st.title("Placeholder data")
        st.markdown("The section below holds placeholder data. It updates ever 4 seconds and loops back to the initial element after 4 iterations.")

        ## Container holding multiple elements
        placeholder = st.empty()

        ## Loop
        while True:
            with placeholder.container():
                ## Json data
                st.json(self.data[self.counter])

                st.divider()

                ## individual elements
                st.subheader(''':red[User ID]''')
                st.text(self.data[self.counter]["userId"])
                st.subheader(''':red[ID]''')
                st.text(self.data[self.counter]["id"])
                st.subheader(''':red[Title]''')
                st.write(self.data[self.counter]["title"])
                st.subheader(''':red[Body]''')
                st.write(self.data[self.counter]["body"])

                ## sleep timer
                time.sleep(5)
                self.counter+=1
                if self.counter > 3:
                    self.counter = 0

if __name__ == "__main__":
    holder = PlaceHolder('https://jsonplaceholder.typicode.com/posts')
    holder.createFrontEnd()
