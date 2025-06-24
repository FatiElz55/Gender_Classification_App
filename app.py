from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('gender_classifier.h5')  # 👈 load your model

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    img = Image.open(file.stream).resize((224, 224)).convert('RGB')  # adapt to your input shape
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0  # 👈 preprocess (adapt to your model)

    prediction = model.predict(x)[0][0]
    gender = "Male" if prediction > 0.5 else "Female"

    return jsonify({'prediction': gender, 'score': float(prediction)})

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)