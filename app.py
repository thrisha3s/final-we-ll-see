from flask import Flask, render_template, request
import pickle
import os

app = Flask(__name__)

model_path = 'model.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    print("Model file not found")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['news']
    prediction = model.predict([text])[0]
    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

