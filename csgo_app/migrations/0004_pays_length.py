# Generated by Django 3.2.7 on 2022-05-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csgo_app', '0003_pays'),
    ]

    operations = [
        migrations.AddField(
            model_name='pays',
            name='length',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
