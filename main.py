import requests
import os
from datetime import datetime as dt
import ivan
import mann
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\Users\mgmma\PycharmProjects\\fitbit-project\\fitbit-e9ff9-firebase-adminsdk-8tpip"
                               "-33e4313c1f.json")
firebase_admin.initialize_app(cred)

default_app = firebase_admin.initialize_app()

date = "2021-02-14"
access_token = os.environ.get("access_token")
endpoint = os.environ.get("endpoint") + date + ".json"
headers = {"Authorization": "Bearer {}".format(access_token)}

response = requests.get(url=endpoint, headers=headers).json()
print(response)
print(f"Ivan's function returned: {ivan.date_and_time()}")
print(f"Mann's function returned: {mann.time_and_level(response)}")
