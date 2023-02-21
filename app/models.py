from django.db import models
from django.conf import settings


class Show(models.Model):
    name_ru = models.TextField()
    show_url = models.URLField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shows')

    def __str__(self):
        return self.name_ru


class ShowInfo(models.Model):
    show = models.OneToOneField(Show, related_name='show_info', on_delete=models.CASCADE, primary_key=True)
    last_episode = models.TextField()
    last_episode_url = models.URLField()
    last_news = models.TextField()
    last_news_url = models.URLField()

    def update_episode_info(self, new_episode, new_episode_url):
        self.last_episode = new_episode
        self.last_episode_url = new_episode_url
        self.save()

    def update_news_info(self, new_news, new_news_url):
        self.last_news = new_news
        self.last_news_url = new_news_url
        self.save()
