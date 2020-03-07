import pyrebase
import json
import os
import requests as r
from base64 import b64encode
import sys
import random


# Variables for the database
config = {
  "apiKey": "AIzaSyBtn1c_Pt3FFvoLcOnhZa3gi0zTO0_mFhA",
  "authDomain": "carbon-footprint-5b239.firebaseapp.com",
  "databaseURL": "https://carbon-footprint-5b239.firebaseio.com",
  "storageBucket": "carbon-footprint-5b239.appspot.com",
  "serviceAccount": "carbon-footprint-5b239-f4444141141f.json"
}

# Initialize the "pyrebase" and retrieve the realtime database
firebase = pyrebase.initialize_app(config)
firebase_db = firebase.database()

# This will be set to some user account
username = "user"
password = "1234"
response = username + " authenticated"

def stream_handler(message):

    print(message["event"]) # put
    print(message["path"]) # /-K7yGTTEp7O549EzTYtI
    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

    firebase_db.child("users").child(username).child("read").set(
        {
            "message": response
        }
    )  

# Get the datastream from the realtime database
data_stream = firebase_db.child("users").child(username).child("post").stream(stream_handler)