from django.shortcuts import render, get_object_or_404
from .models import Album,Song


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk= album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        song_selected = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_msg' : 'you have not selected a valid song.',
        })
    else:
        song_selected.is_favorite = True
        song_selected.save()
        return render(request, 'music/detail.html', {'album': album})