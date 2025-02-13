import json
from flask import Flask, jsonify

app = Flask(__name__)

# Carregar o JSON com os dados
with open('magic/magic.json', 'r') as f:
    items = json.load(f)

@app.route("/getMagic/<int:tag_id>/<string:activity_id>", methods=["GET"])
def getMagic(tag_id, activity_id):
    # Procurar o item correspondente ao tag_id e activity_id fornecidos
    item = next((item for item in items if item["tag_id"] == tag_id and item["activity_id"] == activity_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"tag_id": tag_id, "activity_id": activity_id, "label": item["label"]}), 200

@app.route("/getQuizzes/", methods=["GET"])
def getQuizzes():
    # Retorna a lista de quizzes disponíveis (nome a ser exibido no carrossel)

    return 0

@app.route("/getQuiz/<string:quizName>", methods=["GET"])
def getMagic(quizName):
    # Retorna a lista de quizzes disponíveis (nome a ser exibido no carrossel)

    return 0

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
