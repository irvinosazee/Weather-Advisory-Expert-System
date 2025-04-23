# Weather Advisory Expert System

This project implements a weather advisory expert system that provides context-aware recommendations based on weather conditions and user activities. The system uses decision tables and conditional logic to generate appropriate advisories for various weather scenarios.

## Group 5
## Team Members

- Uyi Osazee Irvin (VUG/SEN/22/8386) - Data Modeling & Testing
- Aneke Olivia.C. (VUG/SEN/22/8304) - User Interface Design (HTML/CSS)
- Babatunde Philip Olutayo (VUG/SEN/22/8575) - Flask Application Development

## Features

- Weather condition assessment based on temperature, humidity, and wind speed
- Activity-specific risk evaluation (daily commute, outdoor sports, travel)
- Seasonal and time-of-day context awareness
- Precipitation and wind advisory generation
- Severity classification of weather conditions
- Web interface for easy interaction

## Project Structure

- `weather_advisory_model.py`: Core expert system model with decision tables
- `app.py`: Flask web application 
- `templates/index.html`: User interface template
- `requirements.txt`: Project dependencies

## Installation

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000/`

## How It Works

The system uses decision tables to classify weather conditions based on temperature, humidity, and wind speed. It then determines the risk level for specific activities under those conditions. Additional factors like precipitation, time of day, and seasonal context are incorporated to provide comprehensive advisories.

### Decision Tables

- General condition table: Maps temperature, humidity, and wind ranges to weather conditions
- Risk level table: Maps weather conditions and activities to risk levels
- Advisory database: Maps conditions and risk levels to specific advice

### Weather Parameters

- Temperature (°C)
- Humidity (%)
- Wind Speed (km/h)
- Precipitation (mm)
- Activity type (daily commute, outdoor sports, travel)
- Month (for seasonal context)

## Data Sources

This system can be connected to weather APIs like:
- NOAA Climate Data
- OpenWeatherMap
- Met Office data

## Future Enhancements

- Integration with live weather APIs
- Historical data analysis for trend-based recommendations
- Location-specific advisories
- Mobile-responsive design improvements

## License

This project is licensed under the MIT License - see the LICENSE file for details.