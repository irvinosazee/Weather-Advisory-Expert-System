import pandas as pd
import numpy as np
from datetime import datetime

class WeatherAdvisorySystem:
    def __init__(self):
        """Initialize the Weather Advisory Expert System with decision tables"""
        # Decision table for general weather conditions
        self.general_condition_table = {
            # Format: (temp_min, temp_max, humidity_min, humidity_max, wind_min, wind_max): "condition"
            (-float('inf'), 0, 0, 100, 0, float('inf')): "freezing",
            (0, 10, 0, 100, 0, float('inf')): "cold",
            (10, 20, 0, 100, 0, float('inf')): "cool",
            (20, 25, 0, 100, 0, float('inf')): "mild",
            (25, 30, 0, 100, 0, float('inf')): "warm",
            (30, 35, 0, 100, 0, float('inf')): "hot",
            (35, float('inf'), 0, 100, 0, float('inf')): "very hot"
        }
        
        # Risk level decision table (weather × activity)
        self.risk_level_table = {
            # Format: (condition, activity): risk_level
            ("freezing", "outdoor_sports"): "high",
            ("freezing", "travel"): "high",
            ("freezing", "daily_commute"): "moderate",
            ("cold", "outdoor_sports"): "moderate",
            ("cold", "travel"): "moderate",
            ("cold", "daily_commute"): "low",
            ("cool", "outdoor_sports"): "low",
            ("cool", "travel"): "low",
            ("cool", "daily_commute"): "low",
            ("mild", "outdoor_sports"): "low",
            ("mild", "travel"): "low",
            ("mild", "daily_commute"): "low",
            ("warm", "outdoor_sports"): "low",
            ("warm", "travel"): "low",
            ("warm", "daily_commute"): "low",
            ("hot", "outdoor_sports"): "moderate",
            ("hot", "travel"): "low",
            ("hot", "daily_commute"): "low",
            ("very hot", "outdoor_sports"): "high",
            ("very hot", "travel"): "moderate",
            ("very hot", "daily_commute"): "moderate"
        }
        
        # Advisory database
        self.advisory_database = {
            # Format: (condition, risk_level): "advisory"
            ("freezing", "high"): "Extreme caution advised. Risk of hypothermia and frostbite. Avoid unnecessary travel and outdoor activities.",
            ("freezing", "moderate"): "Wear multiple layers and cover extremities. Be cautious of ice on roads and pathways.",
            ("freezing", "low"): "Dress warmly and be aware of potentially icy conditions.",
            
            ("cold", "high"): "Limit time outdoors. Wear insulated clothing and protect extremities.",
            ("cold", "moderate"): "Dress in warm layers and be cautious of cold-related discomfort.",
            ("cold", "low"): "Light jacket or sweater recommended.",
            
            ("cool", "high"): "Dress in layers and consider weather-appropriate gear for extended outdoor activities.",
            ("cool", "moderate"): "Light jacket recommended, especially in the evening.",
            ("cool", "low"): "Generally comfortable conditions. Light outer layer may be needed.",
            
            ("mild", "high"): "Comfortable conditions for most activities. Stay hydrated during extended outdoor exposure.",
            ("mild", "moderate"): "Ideal weather for most activities. No special precautions needed.",
            ("mild", "low"): "Optimal conditions for all activities.",
            
            ("warm", "high"): "Stay hydrated and consider sun protection for extended outdoor activities.",
            ("warm", "moderate"): "Comfortable conditions. Consider light clothing and hydration.",
            ("warm", "low"): "Pleasant conditions. No special precautions needed.",
            
            ("hot", "high"): "Limit strenuous activities during peak heat. Stay hydrated and seek shade frequently.",
            ("hot", "moderate"): "Stay hydrated and use sun protection. Take breaks in shade when outdoors.",
            ("hot", "low"): "Light clothing recommended. Stay hydrated.",
            
            ("very hot", "high"): "Heat danger! Avoid strenuous activities. Stay hydrated and in air-conditioned environments when possible.",
            ("very hot", "moderate"): "Minimize sun exposure. Drink plenty of fluids and take frequent breaks in shade or air conditioning.",
            ("very hot", "low"): "Use caution in heat. Stay hydrated and limit direct sun exposure."
        }
        
        # Additional factor modifiers
        self.wind_advisory = {
            (0, 15): "Low wind conditions",
            (15, 30): "Moderate wind. Secure loose objects outdoors.",
            (30, 45): "Strong wind advisory. Be cautious with high-profile vehicles.",
            (45, float('inf')): "Dangerous wind conditions. Avoid unnecessary travel."
        }
        
        self.humidity_comfort = {
            (0, 30): "Very dry conditions. Stay hydrated and moisturize skin.",
            (30, 50): "Comfortable humidity levels.",
            (50, 70): "Moderately humid. May feel warmer than actual temperature.",
            (70, 100): "High humidity. Heat stress possible in warm temperatures."
        }
        
        # Seasonal context
        self.month_seasons = {
            1: "winter", 2: "winter", 3: "spring", 
            4: "spring", 5: "spring", 6: "summer",
            7: "summer", 8: "summer", 9: "fall", 
            10: "fall", 11: "fall", 12: "winter"
        }
        
        # Time of day contexts
        self.time_contexts = {
            (0, 6): "early_morning",
            (6, 10): "morning",
            (10, 14): "midday",
            (14, 18): "afternoon",
            (18, 22): "evening",
            (22, 24): "night"
        }

    def get_condition(self, temperature, humidity, wind_speed):
        """Determine the general weather condition based on parameters"""
        for (temp_min, temp_max, hum_min, hum_max, wind_min, wind_max), condition in self.general_condition_table.items():
            if (temp_min <= temperature < temp_max and 
                hum_min <= humidity < hum_max and 
                wind_min <= wind_speed < wind_max):
                return condition
        return "normal"  # Default condition if no match
    
    def get_risk_level(self, condition, activity):
        """Determine risk level based on condition and activity"""
        key = (condition, activity)
        return self.risk_level_table.get(key, "low")  # Default to low risk if not found
    
    def get_wind_advisory(self, wind_speed):
        """Get appropriate wind advisory based on wind speed"""
        for (min_speed, max_speed), advisory in self.wind_advisory.items():
            if min_speed <= wind_speed < max_speed:
                return advisory
        return "Extreme wind conditions. Seek shelter immediately."
    
    def get_humidity_comfort(self, humidity):
        """Get humidity comfort information"""
        for (min_hum, max_hum), comfort in self.humidity_comfort.items():
            if min_hum <= humidity < max_hum:
                return comfort
        return "Extreme humidity levels. Use caution."
    
    def get_time_context(self, hour=None):
        """Get time of day context"""
        if hour is None:
            hour = datetime.now().hour
            
        for (start_hour, end_hour), context in self.time_contexts.items():
            if start_hour <= hour < end_hour:
                return context
        return "night"  # Default
    
    def get_season_context(self, month=None):
        """Get seasonal context"""
        if month is None:
            month = datetime.now().month
        return self.month_seasons.get(month, "unknown")
    
    def generate_advisory(self, temperature, humidity, wind_speed, activity="daily_commute", 
                          month=None, hour=None, precipitation=0):
        """
        Generate a comprehensive weather advisory based on all parameters
        
        Args:
            temperature (float): Temperature in Celsius
            humidity (float): Humidity percentage (0-100)
            wind_speed (float): Wind speed in km/h
            activity (str): Type of activity (outdoor_sports, travel, daily_commute)
            month (int): Month (1-12), defaults to current month
            hour (int): Hour of day (0-23), defaults to current hour
            precipitation (float): Precipitation amount in mm
            
        Returns:
            dict: Advisory information with multiple components
        """
        # Get base condition and risk level
        condition = self.get_condition(temperature, humidity, wind_speed)
        risk_level = self.get_risk_level(condition, activity)
        
        # Get base advisory
        base_advisory = self.advisory_database.get((condition, risk_level), 
                                             "No specific advisory for these conditions.")
        
        # Get additional context advisories
        wind_advice = self.get_wind_advisory(wind_speed)
        humidity_advice = self.get_humidity_comfort(humidity)
        
        # Add time and seasonal context
        time_context = self.get_time_context(hour)
        season_context = self.get_season_context(month)
        
        # Special precipitation advisories
        precipitation_advice = ""
        if precipitation > 0:
            if precipitation < 2.5:
                precipitation_advice = "Light precipitation expected. Consider carrying an umbrella."
            elif precipitation < 7.5:
                precipitation_advice = "Moderate precipitation expected. Rain gear recommended."
            elif precipitation < 15:
                precipitation_advice = "Heavy precipitation expected. Take precautions against flooding in low areas."
            else:
                precipitation_advice = "Severe precipitation warning. Flooding possible. Avoid unnecessary travel."
        
        # Combine all advice with conditional logic for severe conditions
        severity = "low"
        if risk_level == "high" or wind_speed >= 45 or precipitation >= 15:
            severity = "high"
        elif risk_level == "moderate" or wind_speed >= 30 or precipitation >= 7.5:
            severity = "moderate"
            
        # Combine all advisories
        full_advisory = {
            "condition": condition,
            "risk_level": risk_level,
            "base_advisory": base_advisory,
            "wind_advisory": wind_advice,
            "humidity_advisory": humidity_advice,
            "precipitation_advisory": precipitation_advice if precipitation_advice else "No precipitation expected.",
            "severity": severity,
            "time_context": time_context,
            "season_context": season_context
        }
        
        return full_advisory
    
    def get_text_summary(self, advisory_dict):
        """Convert the advisory dictionary to a readable text summary"""
        summary = f"Weather Advisory: {advisory_dict['condition'].capitalize()} conditions\n\n"
        summary += f"Severity: {advisory_dict['severity'].capitalize()}\n\n"
        summary += f"{advisory_dict['base_advisory']}\n\n"
        
        # Add secondary advisories
        summary += f"• {advisory_dict['wind_advisory']}\n"
        summary += f"• {advisory_dict['humidity_advisory']}\n"
        summary += f"• {advisory_dict['precipitation_advisory']}\n\n"
        
        # Add contextual information
        time_contexts = {
            "early_morning": "early morning",
            "morning": "morning",
            "midday": "midday",
            "afternoon": "afternoon",
            "evening": "evening",
            "night": "night"
        }
        
        time_str = time_contexts.get(advisory_dict['time_context'], advisory_dict['time_context'])
        summary += f"This advisory takes into account {advisory_dict['season_context']} seasonal patterns and {time_str} conditions."
        
        return summary

# Example usage
if __name__ == "__main__":
    advisory_system = WeatherAdvisorySystem()
    # Test for cold, windy day
    advisory = advisory_system.generate_advisory(
        temperature=5,
        humidity=60,
        wind_speed=35,
        activity="travel",
        precipitation=5
    )
    print(advisory_system.get_text_summary(advisory))
    
    # Test for hot summer day
    advisory = advisory_system.generate_advisory(
        temperature=33,
        humidity=75,
        wind_speed=10,
        activity="outdoor_sports",
        precipitation=0
    )
    print("\n" + "-"*50 + "\n")
    print(advisory_system.get_text_summary(advisory))