from celery import shared_task
import time
from app.script import pars_episodes

import django

django.setup()

from app.models import Show, ShowInfo


def send_mail(user, show_name):
    pass


@shared_task
def pars_information():
    all_show = Show.objects.all()
    for show in all_show:
        last_news, last_news_url, last_episode, last_episode_url = pars_episodes(show.show_url)
        if show.show_info.last_episode != last_episode:
            print(f'В сериале {show} вышла новая серия {last_episode}. Посмотрите по ссылке {last_episode_url}')
            show.show_info.last_episode = last_episode
            show.show_info.last_episode_url = last_episode_url
            show.show_info.save()
        elif show.show_info.last_news != last_news:
            print(f'В сериале {show} вышла новая новость - {last_news}. Прочтите её - {last_news_url}')
            show.show_info.update_news_info(last_news, last_news_url)


@shared_task
def print_30_sec():
    for i in range(30):
        print(i)
        time.sleep(1)


@shared_task
def print_20_sec():
    for i in range(20):
        print(i)
        time.sleep(1)
