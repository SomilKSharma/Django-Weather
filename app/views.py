from django.shortcuts import render
import json
import urllib.request

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        key = 'ca98bac4a158672459719889941567c5'
        # api request
        res = urllib.request.urlopen(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}').read()
        json_data = json.loads(res)
        # change ot the dictionary
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'K',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity'])
        }
    else:
        data = {}
    return render(request, 'index.html', data)
