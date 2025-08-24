import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

access_api_key = os.getenv("ACCESS_API_KEY")
access_api_url = os.getenv("ACCESS_API_URL")
access_header = os.getenv("ACCESS_HEADER")

with open("data.json", "r") as file:
    data = json.load(file)

headers = {
    access_header: access_api_key,
    "Content-Type": "application/json"
}

count = 0

for obj in data:
    response = requests.post(access_api_url, json=obj, headers=headers)
    count += 1
    print(response.status_code, count)
