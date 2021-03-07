import time
import ivan
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def time_until_end_of_day(dt=None):
    if dt is None:
        dt = datetime.datetime.now()
    return ((24 - dt.hour - 1) * 60 * 60) + ((60 - dt.minute - 1) * 60) + (60 - dt.second)

cred = credentials.Certificate(
    "C:\\Users\\mgmma\\PycharmProjects\\fitbit-project\\meta-gateway-306808-firebase-adminsdk"
    "-5rwm0-cd89f417a5.json")
# cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': "meta-gateway-306808",
})

db = firestore.client()

while True:
    users_ref = db.collection(u'sleep_datum')
    docs = users_ref.stream()
    alarm_time = ""
    alarm_days = []
    current_time = (int(ivan.time().split(":")[0]) * 60) + int(ivan.time().split(":")[1])
    current_state = ""
    current_day = datetime.datetime.weekday(datetime.datetime.now())
    for doc in docs:
        if doc.id == 'alarm_data':
            alarm_time = (int(doc.to_dict()['time'].split(":")[0]) * 60) + int(doc.to_dict()['time'].split(":")[1])
            alarm_days = doc.to_dict()['days']
        else:
            current_state = doc.to_dict()['state']
    print(alarm_time, alarm_days, current_time, current_state)

    if current_day in alarm_days and (0 < alarm_time - current_time < 30) and current_state == "light":
        #ring alarm
        print('ring alarm')
        #logic error with alarms from midnight to 30 past
    elif current_day not in alarm_days:
        time.sleep(time_until_end_of_day())
        print('no alarm today')
    elif current_time >= alarm_time:
        #ring alarm
        print('ring alarm')
        time.sleep(time_until_end_of_day())
    else:
        time.sleep(60)