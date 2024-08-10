import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
cred = credentials.Certificate('src/firebase.json')
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
