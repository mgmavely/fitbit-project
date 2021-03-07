from tkinter import messagebox
import requests
from tkinter import *
import os
import ivan
import mann
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


BACKGROUND_COLOR = "#B1DDC6"

cred = credentials.Certificate(
    "C:\\Users\\mgmma\\PycharmProjects\\fitbit-project\\meta-gateway-306808-firebase-adminsdk"
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

data = mann.time_and_level(response)


# Read & Write to Google Firestore


def submit_form():
    inp = time.get()
    days = [i for i in range(7) if states[i].get()==1]
    try:
        if (0 <= int(inp[0:2]) < 24) and (0 <= int(inp[3:5]) <= 60) and len(inp) == 5 and len(days) != 0:
            doc_ref = db.collection(u'sleep_datum').document(u'alarm_data')
            doc_ref.set({
                u'time': inp,
                u'days': days
            })
            messagebox.showinfo("Success", "Your alarm has been set!")
            time.delete(0, 'end')
        elif len(days) == 0:
            messagebox.showerror("Failure", "Please select at least one day of the week")
        else:
            messagebox.showerror("Failure", "Invalid time input")
    except ValueError:
        messagebox.showerror("Failure", "Invalid time input")


window = Tk()
window.title("Smart Alarm")
window.config(padx=50, pady=100, bg=BACKGROUND_COLOR)
canvas = Canvas(width=400, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
title = canvas.create_text(200, 50, text="Smart Alarm", font=("Verdana", 40, "bold"), fill="#FFF")

canvas.grid(column=0, row=0, columnspan=7)

time_label = Label(text="Enter Alarm [24h] (HH:MM)", font=("Verdana", 13, "normal"), fg="#FFF", bg=BACKGROUND_COLOR)
time_label.grid(column=1, row=2, columnspan=5)
time = Entry(width=5, justify='center')
time.grid(column=3, row=3, pady=10)

days_label = Label(text="Select days of week for alarm to be active", font=("Verdana", 13, "normal"), fg="#FFF",
                   bg=BACKGROUND_COLOR)
days_label.grid(column=1, row=4, columnspan=7, pady=10)

states = [IntVar() for i in range(7)]

M = Checkbutton(text="M", font=("Verdana", 13, "normal"), fg="#000",
                bg=BACKGROUND_COLOR, variable=states[0])
M.grid(column=0, row=5, pady=10)

T = Checkbutton(text="T", font=("Verdana", 13, "normal"), fg="#000",
                bg=BACKGROUND_COLOR, variable=states[1])
T.grid(column=1, row=5, pady=10)

W = Checkbutton(text="W", font=("Verdana", 13, "normal"), fg="#000",
                bg=BACKGROUND_COLOR, variable=states[2])
W.grid(column=2, row=5, pady=10)

Th = Checkbutton(text="Th", font=("Verdana", 13, "normal"), fg="#000",
                 bg=BACKGROUND_COLOR, variable=states[3])
Th.grid(column=3, row=5, pady=10)

F = Checkbutton(text="F", font=("Verdana", 13, "normal"), fg="#000",
                bg=BACKGROUND_COLOR, variable=states[4])
F.grid(column=4, row=5, pady=10)

S = Checkbutton(text="S", font=("Verdana", 13, "normal"), fg="#000",
                bg=BACKGROUND_COLOR, variable=states[5])
S.grid(column=5, row=5, pady=10)

Sn = Checkbutton(text="Sn", font=("Verdana", 13, "normal"), fg="#000",
                 bg=BACKGROUND_COLOR, variable=states[6])
Sn.grid(column=6, row=5, pady=10)

submit = Button(fg="#FFF", bg="#006400", text="Submit", command=submit_form)
submit.grid(column=3, row=6)

window.mainloop()


