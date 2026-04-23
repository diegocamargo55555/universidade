import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db
from firebase_admin import messaging
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
    
    doc_ref = db.collection("preço").document(id)
    doc_ref.set({"preço": value})

  
    

from firebase_admin import firestore

db = firestore.client()


ex3("bIMyr2crnyOYaMAPOArU", 55)


def ex4():
    
    preco_minimo = 15.00
    produtos_ref = db.collection("produtos_mysql")
    query = produtos_ref.where("preco", ">", preco_minimo).stream()
    
    for doc in query:
        dados = doc.to_dict()
        print(f"Nome: {dados.get('nome')} | Preço: R$ {dados.get('preco'):.2f}")


def ex5():
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'test.appspot.com'
    })
    
    bucket = storage.bucket()
    
    nome_arquivo = "test.txt"
    with open(nome_arquivo, "w") as f:
        f.write("Olá, Firebase Storage!")
    
    blob = bucket.blob(nome_arquivo)
    blob.upload_from_filename(nome_arquivo)
    
    print(f"Arquivo {nome_arquivo} enviado com sucesso.")


def ex6(token, titulo, corpo):
    mensagem = messaging.Message(
        notification=messaging.Notification(
            title=titulo,
            body=corpo,
        ),
        token=token,
    )

    response = messaging.send(mensagem)
    print(f"Sucesso: {response}")

def ex7():
    try:
        user = auth.get_user("uid-inexistente")
        print(user.display_name)
    except exceptions.FirebaseError as e:
        print(f"Erro no Firebase: {e.code} - {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")