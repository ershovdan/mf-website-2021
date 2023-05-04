from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import os
import pathlib


def MainMinecraftPage(request):
    return render(request, 'Minecraft/main_minecraft.html')

def MapMinecraft(request):
    return render(request, 'Minecraft/minecraft_map.html')

def MoreMinecraf(request):
    return render(request, 'Minecraft/minecraft_more.html')

def download(requset):
    file_path = pathlib.Path(r'/opt/dan/modernface_website/media/for_download/MfCraft_Setup.exe')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def download_pack(requset):
    file_path = pathlib.Path(r'/opt/dan/modernface_website/media/for_download/pack_for_MfCraft.zip')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404