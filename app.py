from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response
from utils.eligibility import check_eligibility
from utils.timeline import get_timeline

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

@app.route("/eligibility", methods=["POST"])
def eligibility():
    age = int(request.json.get("age"))
    citizen = request.json.get("citizen")
    result = check_eligibility(age, citizen)
    return jsonify({"result": result})

@app.route("/timeline")
def timeline():
    return jsonify(get_timeline())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)