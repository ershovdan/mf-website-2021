from django.db import models


class Keys(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField(max_length=200)
    key = models.TextField(max_length=19)
    number_of_months = models.IntegerField()
    start_date = models.DateField(auto_now=True)
    activated = models.BooleanField(default=False)


class ForumTopic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=5000, blank=True)
    views = models.IntegerField()
    is_super_topic = models.BooleanField(default=False)
    is_acive = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now=True)
    last_update = models.DateField()
    author = models.TextField(max_length=100)
    number_of_posts = models.IntegerField()
    subject = models.TextField(max_length=5000)


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    topic_id = models.IntegerField()
    text = models.TextField()
    author = models.TextField(max_length=200)
    creation_datetime = models.DateTimeField(auto_now=True)


class Pays(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(auto_now=True)
    email = models.TextField(max_length=150)
    length = models.IntegerField()

