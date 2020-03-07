import pyrebase

# Configuration key for realtime database with all permission (read + write) to true
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

# This will be set to some random user account
username = "ricozhuthegreat"

response = "Hello World!"

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