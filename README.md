# Gender Classification App

This is a simple Flask web application that uses a pre-trained deep learning model to classify the gender of a person from an uploaded image.

---

## 🧠 Purpose

This app demonstrates how to:
- Load and use a `.h5` Keras/TensorFlow model
- Serve it through a Flask web interface
- Let users upload images to get real-time predictions

It’s intended for learning and testing basic image classification in a web environment.

---

## 🛠️ Requirements

Install Python packages before running:

> pip install -r requirements.txt

### Contents of requirements.txt:

Flask
tensorflow
numpy
Pillow
### 🚀 How to Run
#### 1. Clone the repo or download the files:
> git clone https://github.com/FatiElz55/Gender_Classification_App.git
> cd Gender_Classification_App
#### 2. Install dependencies:
> pip install -r requirements.txt
#### 3. Run the Flask app:
>python app.py
Then open your browser and go to:

http://127.0.0.1:5000/ (it may be different for you in general get it throught minikube ip result + 5000 or run minikube service mobilenet-service)
## 📸 How It Works
=> You upload an image (face photo).

=> The model processes it and predicts gender: Male or Female.

=> Result is displayed instantly.

## 🤖 Model Info
=> Type: Convolutional Neural Network (CNN)

=> Trained on: UTKFace Dataset

=> Format: .h5 (Keras/TensorFlow)

## 📌 Notes
For best results, use frontal face images.

You can retrain or replace the model with your own dataset if desired. (check the classification model in this repository: "I'll drop it soon")

## 📧 Contact
For questions or feedback: elzfati55@gmail.com
