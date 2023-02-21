from celery import shared_task
import time
from app.script import pars_episodes, send_subj_mail

import django

django.setup()

from app.models import Show



@shared_task
def pars_information():
    all_show = Show.objects.all()
    for show in all_show:
        last_news, last_news_url, last_episode, last_episode_url = pars_episodes(show.show_url)
        if show.show_info.last_episode != last_episode:
            show.show_info.update_episode_info(last_episode, last_episode_url)
            # show_information = show.show_info
            # show_information.last_episode = last_episode
            # show_information.last_episode_url = last_episode_url
            # show_information.save()
            # show.show_info.last_episode = last_episode
            # show.show_info.last_episode_url = last_episode_url
            # show.show_info.save()
            send_subj_mail(show=show, subject='серия', subj_name=last_episode, url=last_episode_url)

        if show.show_info.last_news != last_news:
            show_information = show.show_info
            show_information.update_news_info(last_news, last_news_url)

            send_subj_mail(show=show, subject='новость', subj_name=last_news, url=last_news_url)

        time.sleep(1)
