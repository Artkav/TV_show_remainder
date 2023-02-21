from django.contrib import admin
from app.models import Show, ShowInfo
# Register your models here.


class ShowAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'show_url')


class ShowInfoAdmin(admin.ModelAdmin):
    list_display = ('show', 'last_episode', 'last_news')


admin.site.register(Show, ShowAdmin)
admin.site.register(ShowInfo, ShowInfoAdmin)
