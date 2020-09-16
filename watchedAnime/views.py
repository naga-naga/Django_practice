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

# 追加完了画面
def added(request):
    # 入力されたデータの読み取り
    title = request.POST["animeTitle"]
    year = request.POST["animeYear"]

    # DB に保存
    ani = Anime(title=title, year=year)
    ani.save()

    return render(request, "watchedAnime/added.html", {
        "title": title,
        "year": year,
    })