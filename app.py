from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
from analysis import generate_dashboard  # For analysis visualizations
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the dataset
data = pd.read_csv('D:\codingenv\ML\Student Depression Pridector\Student Depression Dataset.csv')

# Load the pre-trained model

model = joblib.load('model.joblib')

# Page 1: Project Description
@app.route('/')
def page1():
    return render_template('page1.html')

# Page 2: Analysis Dashboard
@app.route('/dashboard')
def page2():
    # Generate analysis visuals
    dashboard_html = generate_dashboard(data)
    return render_template('page2.html', dashboard_html=dashboard_html)

# Page 3: Prediction Model
@app.route('/predict', methods=['POST'])
def page3():
    if request.method == 'POST':
        try:
            # Extract input features
            form_data = request.form
            input_features = [
                float(form_data['Age']),
                float(form_data['Academic Pressure']),
                float(form_data['Work Pressure']),
                float(form_data['CGPA']),
                float(form_data['Study Satisfaction']),
                float(form_data['Job Satisfaction']),
                float(form_data['Work/Study Hours']),
                float(form_data['Financial Stress']),
                int(form_data['Gender']),
                int(form_data['Dietary Habits']),
                int(form_data['Family History of Mental Illness']),
                int(form_data['Sleep Duration']),
                int(form_data['Suicidal Thoughts']),
            ]

            # Predict
            prediction = model.predict([input_features])  # Wrap in a list to ensure 2D shape
            result = "Depressed" if prediction[0] == 1 else "Not Depressed"

            return jsonify({'result': result})

        except Exception as e:
            return jsonify({'error': str(e)})


