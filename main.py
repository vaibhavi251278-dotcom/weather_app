from api import get_weather

def main():
    print("=== Weather App ===")
    city = input("Enter city name: ")

    weather = get_weather(city)

    if weather is None:
        print("Error: Could not fetch weather data.")
    else:
        print("\n--- Weather Report ---")
        print(f"City: {weather['city']}")
        print(f"Temperature: {weather['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    main()
