import requests
# import streamlit

endpoint = "https://api.lyrics.ovh/v1/GunsN'Roses/Patience"

response = requests.get(endpoint)

print(response)