import os
from flask import Flask, request, render_template, jsonify

from album_art_classifier.predict_model import predict_model
from mlflow.keras import load_model


app = Flask(__name__)

model_uri = os.getenv('MODEL_URI', '')
model = load_model(model_uri)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
	if request.method == 'POST':
		if 'album' not in request.files:
			return 'No file found', 400

		file = request.files['album']
		# TODO: check file type and format etc
		genre = predict_model(model, file)

		return jsonify({'genre': genre})
