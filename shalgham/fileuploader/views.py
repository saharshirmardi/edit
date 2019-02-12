from random import randint
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
import os
import pathlib
from PIL import Image
from django.conf import settings


def index(request):
    return render(request, 'fileuploader/index.html')


def back(request):
    return redirect('/')


def upload(request):
    image = default_storage.save('file.jpg', request.FILES['fileToUpload'])
    context = {'ax': image}
    request.session['Url'] = image
    return render(request, "fileuploader/edit.html", context)


def siasefid(request):
    request.session['Url']
    img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
    imgss = img.convert("L")
    imgss.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
    context = {'ax': request.session['Url']}
    return render(request, 'fileuploader/edit.html', context)


def crop(request):
    try:
        img = Image.open(os.path.join(
            settings.MEDIA_ROOT, request.session['Url']))
        imgcr = img.crop((int(request.POST.get('arz1')), int(request.POST.get(
            'tul1')), int(request.POST.get('arz2')), int(request.POST.get('tul2'))))
        imgcr.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
        context = {'ax': request.session['Url']}
        return render(request, 'fileuploader/edit.html', context)
    except:
        return HttpResponse('eshteba zadi')


def rotate(request):
    try:
        img = Image.open(os.path.join(
            settings.MEDIA_ROOT, request.session['Url']))
        imgrt = img.rotate(int(request.POST.get('zavie')), expand=1)
        imgrt.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
        context = {'ax': request.session['Url']}
        return render(request, 'fileuploader/edit.html', context)
    except:
        return HttpResponse('eshteba zadi')


def resize(request):
    try:
        img = Image.open(os.path.join(
            settings.MEDIA_ROOT, request.session['Url']))
        imgrs = img.resize((int(request.POST.get('andaze1')),
                            int(request.POST.get('andaze2'))))
        imgrs.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
        context = {'ax': request.session['Url']}
        return render(request, 'fileuploader/edit.html', context)
    except:
        return HttpResponse('eshteba zadi')


def share(request):
    path = settings.MEDIA_ROOT
    image_list = os.listdir(path)
    context = {'images': image_list}
    return render(request, 'fileuploader/share.html', context)
