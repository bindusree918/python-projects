import requests

API_KEY = "91de60974c9d16c1e6f925fc282a68df"

print("🌦️ Weather App 🌦️")

city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] != 200:
    print("❌ City not found! Please try again.")
else:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print(f"\n📍 City: {city}")
    print(f"🌡️ Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁️ Condition: {condition}")