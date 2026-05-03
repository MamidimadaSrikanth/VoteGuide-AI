from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response
from utils.eligibility import check_eligibility
from utils.timeline import get_timeline
from functools import lru_cache   # ✅ caching
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# ---- Helpers ----
def safe_json(req):
    try:
        return req.get_json(force=True, silent=True) or {}
    except Exception:
        return {}

def bad_request(msg="Invalid request"):
    return jsonify({"error": msg}), 400


# ---- CACHED FUNCTION ----
@lru_cache(maxsize=10)
def cached_timeline():
    return get_timeline()


# ---- Routes ----
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot responses"""

    data = safe_json(request)
    user_input = (data.get("message") or "").strip()

    if not user_input:
        return bad_request("Message is required")

    try:
        response = chatbot_response(user_input)
        return jsonify({"response": response}), 200
    except Exception:
        return jsonify({"response": "Something went wrong"}), 500


@app.route("/eligibility", methods=["POST"])
def eligibility():
    data = safe_json(request)
    age = data.get("age")
    citizen = (data.get("citizen") or "").strip().lower()

    if age is None:
        return bad_request("Age is required")

    try:
        age = int(age)
    except ValueError:
        return bad_request("Age must be a number")

    if age < 0:
        return bad_request("Invalid age")

    if citizen not in {"yes", "no"}:
        return bad_request("Citizen must be 'yes' or 'no'")

    result = check_eligibility(age, citizen)
    return jsonify({"result": result}), 200


# ---- TIMELINE (CACHED) ----
@app.route("/timeline")
def timeline():
    return jsonify(cached_timeline()), 200


# ---- Entry ----
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)