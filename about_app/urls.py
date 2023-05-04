from django.contrib import admin
from django.urls import path, include
import about_app.views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', about_app.views.MainAbout),
    path('server/', about_app.views.MainServer),
    path('server-api/', about_app.views.ServerInformationView.as_view()),
    path('server_сomponents/', about_app.views.ServerComponents),
]
