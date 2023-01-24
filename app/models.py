from django.db import models
from django.conf import settings


class Serial(models.Model):
    name_en = models.TextField()
    name_ru = models.TextField()
    serial_url = models.URLField()
    serial_img = models.URLField()
    serial_status = models.BooleanField()

    def __str__(self):
        return self.name_ru


class ShowInfo(models.Model):
    show = models.ForeignKey(Serial, related_name='last_information', on_delete=models.CASCADE)
    last_episode_name_ru = models.TextField()
    last_episode_url = models.URLField()
    last_news_name = models.TextField()
    last_news_url = models.URLField()
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='shows_information')
