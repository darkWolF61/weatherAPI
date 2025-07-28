from dotenv import load_dotenv 
import os

load_dotenv()  # Loads variables from .env

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/forecast.json"
