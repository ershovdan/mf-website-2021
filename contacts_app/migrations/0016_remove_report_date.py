# Generated by Django 3.1.3 on 2021-03-05 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0015_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='date',
        ),
    ]