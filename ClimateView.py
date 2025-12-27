#Weather Database
weather_db = {
    "KAMPALA": {"temperature": 23, "condition": "Sunny", "humidity": 60},
    "NAIROBI": {"temperature": 30, "condition": "Rainy", "humidity": 70},
    "KIGALI": {"temperature": 25, "condition": "Cloudy", "humidity": 65}
}

#Visual Display of the cities available in the database
def display_cities():
    print("Available cities in the weather database:")
    for city in weather_db.keys():
        print(f"- {city}")
display_cities()

#Display Menu Options
def display_menu():
    print("\n ============ Menu Options ==============")
    print("1. Get Weather Information")
    print("2. Add City Weather Data")
    print("3. Update City Weather Data")
    print("4. Delete City Weather Data")
    print("5. Exit")
    print("=========================================")

weather_conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Stormy", "Snowy", "Foggy", "Hazy", "Overcast", "Drizzle", "Thunderstorm", "Clear", "Partly Cloudy", "Humid", "Dry", "Misty", "Blizzard", "Sleet", "Gale", "Heatwave", "Cold Snap", "Freezing", "Icy", "Dust Storm", "Tornado", "Hurricane", "Cyclone", "Typhoon", "Monsoon", "Chilly", "Warm", "Cool", "Breezy", "Calm", "Drought", "Flood", "High UV Index", "Low UV Index", "Smoky", "Polluted", "Sultry", "Brisk", "Frosty", "Glacial", "Sweltering", "Balmy", "Nippy", "Raw", "Sizzling", "Scorching", "Muggy", "Temperate", "Variable", "Unsettled", "Stable", "Tepid", "Lukewarm", "Chilly", "Crisp", "Brumal", "Wintry", "Summery", "Autumnal", "Springlike", "Equable", "Inclement", "Pleasant", "Unpleasant", "Mild", "Severe", "Extreme", "Brutal", "Harsh", "Favorable", "Unfavorable", "Torrid", "Frigid", "Sultry", "Balmy", "Nippy", "Raw", "Sizzling", "Scorching", "Muggy", "Temperate", "Variable", "Unsettled", "Stable", "Tepid", "Lukewarm", "Chilly", "Crisp", "Brumal", "Wintry", "Summery", "Autumnal", "Springlike", "Equable", "Inclement", "Pleasant", "Unpleasant", "Mild", "Severe", "Extreme", "Brutal", "Harsh", "Favorable", "Unfavorable", "Torrid", "Frigid", "Sultry", "Balmy", "Nippy", "Raw", "Sizzling", "Scorching", "Muggy", "Temperate", "Variable", "Unsettled", "Stable", "Tepid", "Lukewarm", "Chilly", "Crisp", "Brumal", "Wintry", "Summery", "Autumnal", "Springlike", "Equable", "Inclement", "Pleasant", "Unpleasant", "Mild", "Severe", "Extreme", "Brutal", "Harsh", "Favorable", "Unfavorable", "Torrid", "Frigid", "Sultry", "Balmy", "Nippy", "Raw", "Sizzling", "Scorching", "Muggy", "Temperate", "Variable", "Unsettled", "Stable", "Tepid", "Lukewarm", "Chilly", "Crisp", "Brumal", "Wintry", "Summery", "Autumnal", "Springlike", "Equable", "Inclement", "Pleasant", "Unpleasant", "Mild", "Severe", "Extreme", "Brutal", "Harsh", "Favorable", "Unfavorable", "Torrid", "Frigid"]


#Getting weather information from the database
def get_weather(city):
    if city in weather_db:
        return ("\n"
                f"========== Weather in {city} =============:\n"
                f"Temperature: {weather_db[city]['temperature']}°C\n"
                f"Condition: {weather_db[city]['condition']}\n"
                f"Humidity: {weather_db[city]['humidity']}%")
    else:
        return "City not found in the database."
#Adding, Updating, and Deleting City Weather Data
def add_city_weather(city, temperature, condition, humidity):
    weather_db[city] = {"temperature": temperature, "condition": condition, "humidity": humidity}
    return f"Weather data for {city} added successfully."

def update_city_weather(city, temperature=None, condition=None, humidity=None):
    if city in weather_db:
        if temperature is not None:
            weather_db[city]["temperature"] = temperature
        if condition is not None:
            weather_db[city]["condition"] = condition
        if humidity is not None:
            weather_db[city]["humidity"] = humidity
        return f"Weather data for {city} updated successfully."
    else:
        return "City not found in the database." 
    
def delete_city_weather(city):
    if city in weather_db:
        del weather_db[city]
        return f"Weather data for {city} deleted successfully."
    else:
        return "City not found in the database."

#Main Program Loop
while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        city = input("Enter city name: ").upper()
        weather_info = get_weather(city)
        print(weather_info)
        
    elif choice == '2':
        while True:
            try:
                city = input("Enter city name: ").upper().strip()
                if city in weather_db:
                    print("City already exists in the database.")
                    continue
                elif not city.isalpha():
                    raise ValueError("City name must contain only alphabetic characters.")
            except Exception as e:
                print("Invalid input. Please try again.")
                continue

            while  True:
                try:
                    temperature = int(input("Enter temperature in Celsius: ").strip())
                    if temperature < -100 or temperature > 150:
                        print("Temperature out of realistic range. Please enter a valid temperature.")
                        continue
                    while True:
                        condition = input("Enter weather condition: ").strip().capitalize()
                        if condition not in weather_conditions:
                            print("Invalid weather condition. Please enter a valid condition.")
                            continue
                        break
                    while True:
                        humidity = input("Enter humidity: ").strip()
                        if not humidity.isdigit():
                            print("Invalid input for humidity. Please enter a numeric value.")
                            continue
                        humidity = int(humidity)
                        break
                except ValueError:
                    print("Invalid input for temperature or humidity. Please enter numeric values.")
                    continue
                result = add_city_weather(city, temperature, condition, humidity)
                print(result)
                break
            break
        
    elif choice == '3':
        while True:
            try:    
                city = input("Enter city name: ").upper().strip()
                if city not in weather_db and not city.isalpha():
                    print("City not found in the database or invalid city name.")
                    continue
            except Exception as e:
                print("Invalid input. Please try again.")
                continue
            while True:
                try:
                    temperature = input("Enter new temperature (press Enter to keep current): ").strip()
                    if temperature and (int(temperature) < -100 or int(temperature) > 150):
                        print("Temperature out of realistic range. Please enter a valid temperature or leave blank.")
                        continue
                    temperature = int(temperature) if temperature else None
                    while True:
                        condition = input("Enter new weather condition (press Enter to keep current): ").strip().capitalize()
                        if condition and condition not in weather_conditions:
                            print("Invalid weather condition. Please enter a valid condition or leave blank.")
                            continue
                        condition = condition if condition else None
                        break    
                    while True:
                        humidity = input("Enter new humidity (press Enter to keep current): ").strip()
                        if humidity and not humidity.isdigit():
                            print("Invalid input for humidity. Please enter a numeric value or leave blank.")
                            continue
                        humidity = int(humidity) if humidity else None
                        
                        result = update_city_weather(city, temperature, condition, humidity)
                        print(result)
                        break
                except ValueError:
                    print("Invalid input for temperature or humidity. Please enter numeric values.")
                    continue
                break
        
    elif choice == '4':
        while True:
            try:    
                city = input("Enter city name: ").upper().strip()
                if city not in weather_db and not city.isalpha():
                    print("City not found in the database or invalid city name.")
                    continue
            except Exception as e:
                print("Invalid input. Please try again.")
                continue
            break
        result = delete_city_weather(city)
        print(result)
        
    elif choice == '5' or choice.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")


