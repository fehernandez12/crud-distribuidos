import firebase_admin
from firebase_admin import credentials, firestore

certs = {
    "type": "",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": ""
}

cred = credentials.Certificate(certs)
app = firebase_admin.initialize_app(cred)
database = firestore.client(app)
