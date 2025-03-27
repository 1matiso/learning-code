import requests
from datetime import datetime

USERNAME = "matheust"
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "ghostmice4"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": "matheust",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Dev Graph",
    "unit": "Classes",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year = 2024, month = 12, day = 15)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "0",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
