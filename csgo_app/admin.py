from django.contrib import admin
from .models import Keys, ForumTopic, Posts


class KeysShow(admin.ModelAdmin):
    list_display = ('id', 'username', 'key', 'number_of_months', 'start_date', 'activated')


class ForumTopics(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'is_acive', 'is_super_topic', 'views', 'last_update')


class PostsShow(admin.ModelAdmin):
    list_display = ('id', 'topic_id', 'author', 'creation_datetime')


admin.site.register(Keys, KeysShow)
admin.site.register(ForumTopic, ForumTopics)
admin.site.register(Posts, PostsShow)