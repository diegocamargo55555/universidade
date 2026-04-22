import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

# EX 1
cred = credentials.Certificate("cddt3-eff63-firebase-adminsdk-fbsvc-59878a4357.json")
app = firebase_admin.initialize_app(cred)
print(app)



# ex 2


user = auth.create_user(
 email="user@example.com",
 password="password",
 display_name="H"
)
print(f"UID: {user.uid}")


# EX 3
def ex3():
    print("\nEX 3 ")
    # Obter referência
    ref = db.reference("/usersprodutos_mysql/bIMyr2crnyOYaMAPOArU")

    # Ler dados
    data = ref.get()

    # Escrever dados
    ref.set({"preço": "55"})

    # Atualizar campos
    ref.update({"preço": 55})

    # Deletar
    ref.delete()

#ex3()
