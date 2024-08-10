import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
cred = credentials.Certificate('src\sarasaihack-firebase-adminsdk-8bmuc-f00c1f7f00.json')
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
