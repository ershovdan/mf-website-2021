from django.urls import path, include
import minecraft_app.views

urlpatterns = [
    path('', minecraft_app.views.MainMinecraftPage, name='minecraft'),
    path('download/', minecraft_app.views.download, name='download'),
    path('download_pack/', minecraft_app.views.download_pack, name='download_pack'),
    path('map/', minecraft_app.views.MapMinecraft, name='minecraft_map'),
    path('more/', minecraft_app.views.MoreMinecraf, name='minecraft_more'),
]