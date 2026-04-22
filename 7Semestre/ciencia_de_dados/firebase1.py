import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

# EX 1
cred = credentials.Certificate("cddt3-eff63-firebase-adminsdk-fbsvc-59878a4357.json")
app = firebase_admin.initialize_app(cred)
print(app)



# ex 2

def ex2():
    user = auth.create_user(
     email="user@example.com",
     password="password",
     display_name="H"
    )
    print(f"UID: {user.uid}")

#ex2()

# EX 3
def ex3(id, value):
    print("\nEX 3 ")
    # Obter referência
    
    doc_ref = db.collection("preço").document(id)
    doc_ref.set({"preço": value})

    

from firebase_admin import firestore

db = firestore.client()


ex3("bIMyr2crnyOYaMAPOArU", 55)
