from django.urls import path
import weather_app.views


urlpatterns = [
    path('', weather_app.views.MainWeather),
]
