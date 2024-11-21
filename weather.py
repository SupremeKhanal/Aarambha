import requests

def get_weather_data(city, api_key):
    MAIN_URL = "http://api.openweathermap.org/data/2.5/weather?"
    URL = f"{MAIN_URL}appid={api_key}&q={city}&units=metric"  # Using metric for Celsius
    response = requests.get(URL)

 

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        return temperature, humidity, weather_description
    else:
        print("Error fetching data:", response.status_code)
        return None, None, None

def interpret_weather(temperature, humidity, weather_description):
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {weather_description.capitalize()} possiblity")

def main():
    city = "Kathmandu"  # You can change this to any city
    api_key = "00470ca870b8b4ed4afd09915de7a567"  # Replace with your OpenWeatherMap API key

    temperature, humidity, weather_description = get_weather_data(city, api_key)
    if temperature is not None:
        interpret_weather(temperature, humidity, weather_description)

if __name__ == "__main__":
    main()
    