from django.urls import path
import other_app.views


urlpatterns = [
    path('', other_app.views.MainOther),
    path('rockets/', other_app.views.MainRockets),
    path('software/', other_app.views.MainSoftware),
    path('rockets/r1/', other_app.views.r1Page),
    # path('rockets/r2/', other_app.views.r2Page),
    path('rockets/artemis/', other_app.views.artemisPage),
    path('rockets/engines/e1/', other_app.views.gremlin_e1Page),
    path('weather-api/', other_app.views.WeatherInformationView.as_view()),
    path('articles/', other_app.views.articles),
    path('articles/spacex_raptor', other_app.views.spacex_raptor),
]