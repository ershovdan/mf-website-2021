from django.shortcuts import render


def MainWeather(request):
    return render(request, 'Weather/main_weather.html')