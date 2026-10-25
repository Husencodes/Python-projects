import requests

API_KEY = "YOUR_API_KEY" #add your own api key from weather app


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        print("\n------ WEATHER REPORT ------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels like:", data["main"]["feels_like"], "°C")
        print("Condition:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind speed:", data["wind"]["speed"], "m/s")
        print("----------------------------")

    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print("Invalid API key. Check your API key.")
        elif response.status_code == 404:
            print("City not found. Please check the name.")
        else:
            print("Weather service returned an error.")

    except requests.exceptions.RequestException:
        print("Network error. Check your internet connection.")

    except (KeyError, IndexError, ValueError):
        print("Unable to read weather data.")


while True:
    city = input("\nEnter city name (or type exit): ").strip()

    if city.lower() == "exit":
        print("Thank you for using Weather App!")
        break

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")
