import requests
import os
import getpass
from datetime import datetime

password = os.environ['password']
passcode = getpass.getpass('Enter Password:')

if passcode != password:
  print("Incorrect password")
  os._exit(0)
  
USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPH_ID = "graph01"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Morning Walk",
    "unit": "KM",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Kathmandu",
}

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

"""
today = datetime.now()
# For specific date
# today = datetime(year=2023, month=2, day=22)
today_date = today.strftime("%Y%m%d")
"""

############ Date validation and input ################
date_input = input("Enter date(yyyy-mm-dd): ")
date_format = '%Y-%m-%d'
try:
   # formatting the date using strptime() function
   dateObject = datetime.strptime(date_input, date_format)
   formated_date = dateObject.strftime("%Y%m%d")

# If the date validation goes wrong
except ValueError:
   # printing the appropriate text if ValueError occurs
   print("Incorrect data format, should be YYYY-MM-DD")
   os._exit(0)

pixel_data = {
    "date": formated_date,
    "quantity": input("Enter how many kilometers have you travelled today?: "),
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
print(f"View your graph in: {pixel_creation_endpoint}.html")


"""
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# -------- UPDATE PIXEL ------
date = "20230221"
update_endpoint = f"{pixel_creation_endpoint}/{date}"
update_data = {
    "quantity": "8"
}

response = requests.put(url=update_endpoint, headers=headers, json=update_data)

# -------- DELETE PIXEL ------
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
"""
