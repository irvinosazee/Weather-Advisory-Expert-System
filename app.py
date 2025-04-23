from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from datetime import datetime
import joblib
import os

# Import our weather advisory model
from weather_advisory_model import WeatherAdvisorySystem

app = Flask(_name_)

# Initialize the model
advisory_system = WeatherAdvisorySystem()

@app.route('/')
def index():
    """Render the main page of the application"""
    return render_template('index.html')

@app.route('/get_advisory', methods=['POST'])
def get_advisory():
    """Process form data and return weather advisory"""
    try:
        # Get form data
        temperature = float(request.form.get('temperature', 20))
        humidity = float(request.form.get('humidity', 50))
        wind_speed = float(request.form.get('wind_speed', 10))
        activity = request.form.get('activity', 'daily_commute')
        precipitation = float(request.form.get('precipitation', 0))
        
        # Use current month and hour if not specified
        now = datetime.now()
        month = int(request.form.get('month', now.month))
        hour = int(request.form.get('hour', now.hour))
        
        # Generate advisory
        advisory = advisory_system.generate_advisory(
            temperature=temperature,
            humidity=humidity,
            wind_speed=wind_speed,
            activity=activity,
            month=month,
            hour=hour,
            precipitation=precipitation
        )
        
        # Get text summary
        text_summary = advisory_system.get_text_summary(advisory)
        
        # Prepare response
        response = {
            'summary': text_summary,
            'details': advisory,
            'success': True
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if _name_ == '_main_':
    app.run(debug=True)