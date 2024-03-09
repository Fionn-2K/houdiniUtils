import json
import pandas as pd
import requests
import streamlit as st
import time


## Send a get request to the desired URL
response = requests.get('https://jsonplaceholder.typicode.com/posts')

data = response.json()

## write data to json file
with open("placeholder_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("Json file created")


st.title("Placeholder data")

# ## display json content
# st.json({"userId": 1,
#         "id": 1,
#         "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#         "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
#          })

# ## open json file
# with open("placeholder_data.json", "r") as jfile:
#     file = json.load(jfile)
#     df = pd.json_normalize(file, meta=[
#         "userId",
#         "id",
#         "title",
#         "body"
#     ])
# df
