from flask import Flask, jsonify
import random
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

firebase_cred = {
    "type": "service_account",
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
}

cred = credentials.Certificate(firebase_cred)
firebase_admin.initialize_app(cred)

db = firestore.client()

items = ["cat", "dog", "alligator", "elephant", "tiger", "lion"]

@app.route("/getMagic/<int:id>", methods=["GET"])
def getMagic(id):
    random_item = random.choice(items)

    magic_request_ref = db.collection('magic_requests').add({
        'id': id,
        'item': random_item
    })

    return jsonify({"id": id, "item": random_item}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
