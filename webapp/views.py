from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.

def index(request):
    city = request.GET.get('city', 'Cairo')
    api_url = f"{settings.WEATHER_API_URL}?key={settings.WEATHER_API_KEY}&q={city}&lang=en"
    
    response = requests.get(api_url)

    # ----
    url = f"http://api.weatherapi.com/v1/search.json?key={settings.WEATHER_API_KEY}&q={city}"
    response1 = requests.get(url)
    data1 = response1.json()

    if len(data1) > 0:
        for city_data in data1:
            print(f"City: {city_data['name']}, Country: {city_data['country']}")
    else:
        print("No matching cities found.")
    # ----

    if response.status_code == 200:
        data = response.json()
        context = {
            'city': city,
            'temperature': data['current']['temp_c'],
            'description': data['current']['condition']['text'],
            'icon': data['current']['condition']['icon'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph'],
        }
    else:
        context = {'error': 'Sorry, the request was not found or there is an error in the request'}

    return render(request, 'index.html', context)