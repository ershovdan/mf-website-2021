from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from pathlib import Path

def MainOther(request):
    return render(request, 'Other/main_other.html')

def MainRockets(request):
    return render(request, 'Other/main_rockets.html')

def MainSoftware(request):
    return render(request, 'Other/software/main_software.html')

def r1Page(request):
    return render(request, 'Other/rockets/r1.html')

def r2Page(request):
    return render(request, 'Other/rockets/r2.html')

def artemisPage(request):
    return render(request, 'Other/rockets/artemis.html')

def gremlin_e1Page(request):
    return render(request, 'Other/rockets/gremlin_e1.html')


def articles(request):
    return render(request, 'Other/articles/main.html')


def spacex_raptor(request):
    return render(request, 'Other/articles/spacex_raptor.html')


class WeatherInformationView(APIView):
    def get(self, request):
        with open(Path('/home/ershovdan/My projects/QOTWS/weather/forecast.json'), 'r') as ForecastFile_:
            ForecastFileJson = json.load(ForecastFile_)

        with open(Path('/home/ershovdan/My projects/QOTWS/weather/last_weather.json'), 'r') as LastWeatherFile_:
            LastWeatherFileJson = json.load(LastWeatherFile_)

        context_final = {'last_weather': LastWeatherFileJson, 'forecast': ForecastFileJson}
        return Response(context_final)