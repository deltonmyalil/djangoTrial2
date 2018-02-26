# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.template import loader
from django.shortcuts import render
from django.http import Http404


# Create your views here.

def index(request):
    all_photos = Photo.objects.all()
    '''
    html = ''
    for photo in all_photos:
        url = '/photos/' + str(photo.id) + '/'
        html += ' <a href="' + url + '">' + str(photo.name) + '</a><br>'
    #Deleted this and replaced with html template
    '''
    template = loader.get_template('photoapp/index.html')
    context = {
        'all_photos': all_photos
    }
    # return HttpResponse(template.render(context,request))  # instead of HttpResponse, use render()
    return render(request, 'photoapp/index.html', context)


def detail(request, photo_id):
    # return HttpResponse("<h2> This is the page for Photo" + str(photo_id) + "</h2>")  #This is static
    try:
        photo = Photo.objects.get(id=photo_id)
    except Photo.DoesNotExist:
        raise Http404('Photo not found')
    return render(request, 'photoapp/detail.html', {'photo': photo})
