import requests
import streamlit

endpoint = "https://api.lyrics.ovh/v1/acdc/hellsbells"

response = requests.get(endpoint)

print(response)