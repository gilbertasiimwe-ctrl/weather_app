#Weather Database
weather_db = {
    "KAMPALA": {"temperature": 23, "condition": "Sunny", "humidity": 60},
    "NAIROBI": {"temperature": 30, "condition": "Rainy", "humidity": 70},
    "KIGALI": {"temperature": 25, "condition": "Cloudy", "humidity": 65}
}
#Getting weather information from the database

def get_weather(city):
    if city in weather_db:
        info = weather_db[city]
        



