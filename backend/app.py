import pyrebase

# Variables for the database
config = {
  "apiKey": "AIzaSyBtn1c_Pt3FFvoLcOnhZa3gi0zTO0_mFhA",
  "authDomain": "carbon-footprint-5b239.firebaseapp.com",
  "databaseURL": "https://carbon-footprint-5b239.firebaseio.com",
  "storageBucket": "carbon-footprint-5b239.appspot.com",
  "serviceAccount": "carbon-footprint-5b239-f4444141141f.json"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": ""
}

# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])

user = auth.sign_in_with_email_and_password(email, password)
# before the 1 hour expiry:
user = auth.refresh(user['refreshToken'])
# now we have a fresh token
user['idToken']