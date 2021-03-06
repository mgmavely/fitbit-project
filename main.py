import requests
import os
from datetime import datetime as dt

date = "2021-02-14"
access_token = os.environ.get("access_token")
endpoint = os.environ.get("endpoint") + date + ".json"
headers = {"Authorization": "Bearer {}".format(access_token)}

response = requests.get(url=endpoint, headers=headers).json()
print(response)