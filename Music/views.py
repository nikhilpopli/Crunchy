#from django.http import HttpResponse
#from django.template import loader
#from django.http import Http404
#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Album

def index(request):
    #template = loader.get_template('Music/index.html')
    all_albums = Album.objects.all()
    context = {
        'all_albums':all_albums,
    }
    return render(request, 'Music/index.html', context)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'Music/detail.html', {'album':album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected = album.song_set.get(pk=request.POST['song'])
    except:
        context = {
            'album':album,
            'error_msg':'Something went wrong!!!'
        }
        return render(request, 'Music/detail.html', context)
    else:
        if(selected.is_favorite):
            selected.is_favorite=False
        else:
            selected.is_favorite=True
        selected.save()
        return render(request, 'Music/detail.html', {'album':album})
