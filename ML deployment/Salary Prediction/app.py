from flask import Flask, render_template, request
import pickle
import numpy as np

# Create an object of the Flask
app = Flask(__name__)

# Load the ML models and polyconvertor
LinearRegressor_model = pickle.load(open('models/linearRegressor.pkl', 'rb'))
PolyRegressor_model = pickle.load(open('models/polyRegressor.pkl', 'rb'))
polyConvertor = pickle.load(open('models/feature_polyconvertor.pkl', 'rb'))

# Set the url '/' to exceute the function "home".
@app.route('/')
def home():
	return render_template('index.html')

# Set the url '/predict' to excuete the function "predict"
@app.route('/predict', methods=['POST'])
def predict():
    selected_model = request.form.get('model')
    feature = [float(request.form['Position'])]
    
    if selected_model == 'PolynomialRegression':
        prediction = PolyRegressor_model.predict(polyConvertor.transform([feature]))
        return render_template('index.html', Prediction_text='Salary of Position is USD$ {:.2f}'.format(prediction[0]))
    if selected_model == 'LinearRegression':
        prediction = LinearRegressor_model.predict([feature])
        return render_template('index.html', Prediction_text='Salary of Position is USD$ {:.2f}'.format(prediction[0]))
    

if __name__ == "__main__":
	app.run()