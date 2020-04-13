from django.shortcuts import render
import requests
def home(request):
	if request.method == 'POST':
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=cc355cd2dc64c8cf41bad66b64e790f2'
		city = 'Delhi'
		#city = request.POST.get('place')
		r = requests.get(url.format(city)).json()

		city_weather = {

			'city':city,
			'temperature':r['main']['temp'],
			'desc' : r['weather'][0]['description'],
			'icon' : r['weather'][0]['icon']

		}

		

		context = {'city_weather': city_weather}
		return render(request,'app/home.html',context)
	else:
		return render(request,'app/home.html')
# Create your views here.
