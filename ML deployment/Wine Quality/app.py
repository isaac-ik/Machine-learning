"""
Created on Wed Apr 17 14:29:47 2024
Updated on Wed Jan 15 14:30:45 2025
@author: isaacik
"""

from flask import Flask, render_template, request
import pickle
import numpy as np

# Create a WSGI object
wineApp = Flask(__name__)

# Load models
sc = pickle.load(open('models/StandardScaler.pkl', 'rb'))
lr = pickle.load(open('models/LinearRegressor.pkl', 'rb'))

# Create end points
@wineApp.route('/')
@wineApp.route('/home')
def home():
    return render_template('index.html')

@wineApp.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['residual_sugar']),
            float(request.form['chlorides']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['density']),
            float(request.form['pH']),
            float(request.form['sulphates']),
            float(request.form['alcohol'])
        ]
        # Reshape for the scaler
        features_array = np.array(features).reshape(1, -1)
        feat = sc.transform(features_array)
        y_pred = lr.predict(feat)

        return render_template('predictionPage.html', Prediction_text=f'Quality of the wine is {y_pred[0]:.2f}')
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    wineApp.run(debug=True)
