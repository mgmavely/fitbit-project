import requests
import os
import ivan
import mann
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("C:\\Users\\mgmma\\PycharmProjects\\fitbit-project\\meta-gateway-306808-firebase-adminsdk"
                               "-5rwm0-cd89f417a5.json")
# cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': "meta-gateway-306808",
})

db = firestore.client()

date = "2021-02-14"
access_token = os.environ.get("access_token")
endpoint = os.environ.get("endpoint") + date + ".json"
headers = {"Authorization": "Bearer {}".format(access_token)}

response = requests.get(url=endpoint, headers=headers).json()
print(response)

data = mann.time_and_level(response)

print(f"Ivan's function returned: {ivan.date_and_time()}")
print(f"Mann's function returned: {mann.time_and_level(response)}")

#Read & Write to Google Firestore

# doc_ref = db.collection(u'sleep_datum').document(u'sleep_data')
# doc_ref.set({
#     u'time': "Fuck",
#     u'state': "you"
# })
#
# users_ref = db.collection(u'sleep_datum')
# docs = users_ref.stream()
#
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
