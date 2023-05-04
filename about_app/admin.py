from django.contrib import admin
from .models import ServerInformation_24h

class Server(admin.ModelAdmin):
    list_display = ['id', 'cpu', 'cpu_freq', 'ram', 'time', 'date']

admin.site.register(ServerInformation_24h, Server)



