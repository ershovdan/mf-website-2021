import django
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from djangoProject2 import settings
from django.conf.urls import handler404, url, handler500
from main_app import views as main_app_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
import about_app.views



urlpatterns = [
    path('administrate_page/', admin.site.urls, name="admin"),
    path('', include('main_app.urls'), name='MainPage'),
    path('accounts/', include('account_app.urls')),
    path('news/', include('news_app.urls')),
    path('weather/', include('weather_app.urls')),
    path('contacts/', include('contacts_app.urls')),
    path('about/', include('about_app.urls')),
    path('EULA/', main_app_views.EULA_page, name="EULA"),
    path('minecraft/', include('minecraft_app.urls')),
    path('csgo/', include('csgo_app.urls')),
    path('other/', include('other_app.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/logo/mf/mf.ico'))),
    path('server-api/', include('rest_framework.urls', namespace='rest_framework')),
]

handler404 = 'main_app.views.handler404'
handler500 = 'main_app.views.handler500'


