from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app.models import Show, ShowInfo
from app.script import pars_episodes, get_data


def index(request):
    return render(request, 'app/index.html', context={})


def pars_shows(request):
    search_str = request.POST.get('search_str')
    shows = get_data(search_str)
    return render(request, 'app/index.html', context={'shows': shows})


def add_to_list(request):
    url = request.POST.get('url')
    name_ru = request.POST.get('name_ru')

    new_show, created = Show.objects.get_or_create(
        name_ru=name_ru,
        show_url=url
    )
    new_show.users.add(request.user)

    if created:
        print('new was created')
        last_news, last_news_url, last_episode, last_episode_url = pars_episodes(url)
        print(last_news)
        print(last_episode)
        new_show_info = ShowInfo(
            last_episode=last_episode,
            last_episode_url=last_episode_url,
            last_news=last_news,
            last_news_url=last_news_url,
            show=new_show,
        )
        new_show_info.save()

    return redirect('index')
