from datetime import datetime, timezone
import requests

weather_25_url_jkt = "https://api.openweathermap.org/data/2.5/onecall?lat=-6.2146&lon=106.8451&units=metric&appid=5796abbde9106b7da4febfae8c44c232"

response = requests.get(weather_25_url_jkt)
data = response.json()

print("Weather Forecast:")
for i in range(6):
    utc_date = datetime.fromtimestamp(
        data['daily'][i]['dt'], timezone.utc).strftime('%a, %d %b %Y')
    temp = data['daily'][i]['temp']['day']
    print(f"{utc_date}: {temp}°C")
