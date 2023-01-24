from django.http import HttpResponseRedirect
from django.shortcuts import render
from app.models import Serial, ShowInfo
from app.script import pars_episodes


def index(request):
    serials = Serial.objects.all()
    return render(request, 'app/index.html', context={'serials': serials})


def add_to_list(request, pk):
    show = Serial.objects.get(pk=pk)
    last_news, last_news_url, last_episode, last_episode_url = pars_episodes(show.serial_url)
    new_show_info, created = ShowInfo.objects.get_or_create(
        show=show,
        last_episode_name_ru=last_episode,
        last_episode_url=last_episode_url,
        last_news_name=last_news,
        last_news_url=last_news_url,
    )
    new_show_info.users.add(request.user)
    print(f'Add user {request.user} to ShowInfo for show named: {new_show_info.show}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
