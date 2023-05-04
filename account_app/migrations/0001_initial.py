# Generated by Django 3.1.7 on 2021-03-25 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=1000)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('gender', models.CharField(blank=True, default='unknown', max_length=20)),
                ('age', models.CharField(blank=True, default='unknown', max_length=20)),
                ('city', models.CharField(blank=True, default='unknown', max_length=100)),
                ('avatar', models.ImageField(blank=True, default='avatars/default_avatar.jpg', upload_to='avatars')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
