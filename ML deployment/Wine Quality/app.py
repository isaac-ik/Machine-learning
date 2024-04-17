# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:29:47 2024

@author: isaacik
"""

from flask import Flask, render_template, request
import pickle

# Create a WSGI object
wineApp = Flask(__name__)

# Load models
sc = pickle.load(open('models/StandardScaler.pkl', 'rb'))
lr = pickle.load(open('models/LinearRegressor.pkl', 'rb'))

# Create end points
@wineApp.route('/home')
def home():
    return render_template('index.html')

@wineApp.route('/predict', methods=['GET', 'POST'])
def predict():
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
    feat = sc.transform(features)
    y_pred = lr.predict(feat)
    return render_template('predictionPage.html', Prediction_text='Quality of the wine is {:.2f}'.format(y_pred[0]))

if __name__ == "__main__":
    wineApp.run()