import json
from flask import Flask, jsonify

app = Flask(__name__)

with open('magic/magic.json', 'r') as f:
    items = json.load(f)

@app.route("/getMagic/<int:tag_id>/<string:activity_id>", methods=["GET"])
def getMagic(tag_id, activity_id):
    item = next((item for item in items if item["tag_id"] == tag_id and item["activity_id"] == activity_id), None)

    if item is None:
        return jsonify({"error": "Item not found"}), 404

    return jsonify({"tag_id": tag_id, "activity_id": activity_id, "label": item["label"]}), 200

@app.route("/getQuizzes/", methods=["GET"])
def getQuizzes():
    try:
        with open("magic/magic.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
        quizzes = [
            {"label": item["label"], "tag_id": item["tag_id"]}
            for item in data if item.get("activity_id") == "quiz"
        ]
        
        return jsonify(quizzes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/getQuiz/<string:quizName>", methods=["GET"])
def getQuiz(quizName):
    try:
        with open("quiz/animals.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
        quiz_data = {
            "quiz_name": quizName,
            "questions": data
        }
        
        return jsonify(quiz_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
