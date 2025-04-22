# app.py
from flask import Flask, render_template, request, jsonify
import joblib
import os
import numpy as np
from datetime import datetime

app = Flask(_name_)

# Load the weather advisory model
model_path = os.path.join('models', 'weather_advisory_system.pkl')
weather_system = None

try:
    weather_system = joblib.load(model_path)
except:
    print("Model file not found. Make sure to train the model first.")

@app.route('/')
def index():
    """Render the main page of the application."""
    # Get current month for default value
    current_month = datetime.now().month
    return render_template('index.html', current_month=current_month)

@app.route('/get_advisory', methods=['POST'])
def get_advisory():
    """Process form data and return weather advisory."""
    if weather_system is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.'
        }), 500
    
    try:
        # Get form data
        temperature = float(request.form.get('temperature', 0))
        humidity = float(request.form.get('humidity', 0))
        wind_speed = float(request.form.get('wind_speed', 0))
        month = int(request.form.get('month', datetime.now().month))
        
        # Generate advisory using the loaded model
        advisory = weather_system.flask_generate_advisory(temperature, humidity, wind_speed, month)
        
        # Return the advisory
        return jsonify(advisory)
    
    except Exception as e:
        return jsonify({
            'error': f'Error generating advisory: {str(e)}'
        }), 500

@app.route('/about')
def about():
    """Render the about page with information about the system."""
    return render_template('about.html')

if _name_ == '_main_':
    app.run(debug=True) # app.py
from flask import Flask, render_template, request, jsonify
import joblib
import os
import numpy as np
from datetime import datetime

app = Flask(_name_)

# Load the weather advisory model
model_path = os.path.join('models', 'weather_advisory_system.pkl')
weather_system = None

try:
    weather_system = joblib.load(model_path)
except:
    print("Model file not found. Make sure to train the model first.")

@app.route('/')
def index():
    """Render the main page of the application."""
    # Get current month for default value
    current_month = datetime.now().month
    return render_template('index.html', current_month=current_month)

@app.route('/get_advisory', methods=['POST'])
def get_advisory():
    """Process form data and return weather advisory."""
    if weather_system is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.'
        }), 500
    
    try:
        # Get form data
        temperature = float(request.form.get('temperature', 0))
        humidity = float(request.form.get('humidity', 0))
        wind_speed = float(request.form.get('wind_speed', 0))
        month = int(request.form.get('month', datetime.now().month))
        
        # Generate advisory using the loaded model
        advisory = weather_system.flask_generate_advisory(temperature, humidity, wind_speed, month)
        
        # Return the advisory
        return jsonify(advisory)
    
    except Exception as e:
        return jsonify({
            'error': f'Error generating advisory: {str(e)}'
        }), 500

@app.route('/about')
def about():
    """Render the about page with information about the system."""
    return render_template('about.html')

if _name_ == '_main_':
    app.run(debug=True)
