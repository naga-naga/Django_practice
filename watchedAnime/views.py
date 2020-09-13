from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Anime

# Create your views here.
# メイン画面
def index(request):
    anime_list = Anime.objects.all()
    template = loader.get_template("watchedAnime/index.html")
    context = {
        "anime_list": anime_list,
    }
    return HttpResponse(template.render(context, request))

# アニメ追加画面
def register(request):
    return render(request, "watchedAnime/register.html")