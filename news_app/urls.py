from django.urls import path, include
import main_app
import news_app.views

urlpatterns = [
    path('', news_app.views.News, name="news"),
]