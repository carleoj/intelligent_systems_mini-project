from flask import Flask, request, jsonify
from joblib import load
import numpy as np
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Flask server is running!"

# ---------------------------
# Load models and features
# ---------------------------
stress_model = load("Stress_Model_XGBoost.joblib")
anxiety_model = load("Anxiety_Model_LightGBM.joblib")
depression_model = load("Depression_Model_XGBoost.joblib")

@app.route("/predict_stress", methods=["POST"])
def predict_stress():
    data = request.get_json()
    stress_array = np.array([data["data"]])
    stress_pred = int(stress_model.predict(stress_array)[0])
    return jsonify({"Predicted_Stress_Level": stress_pred + 1})

@app.route("/predict_anxiety", methods=["POST"])
def predict_anxiety():
    data = request.get_json()
    anxiety_array = np.array([data["data"]])
    anxiety_pred = int(anxiety_model.predict(anxiety_array)[0])
    return jsonify({"Predicted_Anxiety_Level": anxiety_pred + 1})

@app.route("/predict_depression", methods=["POST"])
def predict_depression():
    data = request.get_json()
    depression_array = np.array([data["data"]])
    depression_pred = int(depression_model.predict(depression_array)[0])
    return jsonify({"Predicted_Depression_Level": depression_pred + 1})

if __name__ == '__main__':
    app.run(debug=True)
