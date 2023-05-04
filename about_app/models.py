from django.db import models

class ServerInformation(models.Model):
    cpu = models.IntegerField(blank=True)
    cpu_freq = models.IntegerField(blank=True)
    ram = models.IntegerField(blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    ts = models.DateTimeField(auto_now_add=True)

class ServerInformation_15m(models.Model):
    cpu = models.IntegerField(blank=True)
    cpu_freq = models.IntegerField(blank=True)
    ram = models.IntegerField(blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    ts = models.DateTimeField(auto_now_add=True)

class ServerInformation_30m(models.Model):
    cpu = models.IntegerField(blank=True)
    cpu_freq = models.IntegerField(blank=True)
    ram = models.IntegerField(blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    ts = models.DateTimeField(auto_now_add=True)

class ServerInformation_1h(models.Model):
    cpu = models.IntegerField(blank=True)
    cpu_freq = models.IntegerField(blank=True)
    ram = models.IntegerField(blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    ts = models.DateTimeField(auto_now_add=True)

class ServerInformation_6h(models.Model):
    cpu = models.IntegerField(blank=True)
    cpu_freq = models.IntegerField(blank=True)
    ram = models.IntegerField(blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    ts = models.DateTimeField(auto_now_add=True)

class ServerInformation_24h(models.Model):
    cpu = models.IntegerField(blank=True)
    cpu_freq = models.IntegerField(blank=True)
    ram = models.IntegerField(blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    ts = models.DateTimeField(auto_now_add=True)