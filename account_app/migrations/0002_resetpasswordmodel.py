# Generated by Django 3.2.3 on 2021-06-15 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPasswordModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_checked', models.BooleanField(blank=True, default=False)),
                ('code_send', models.BooleanField(blank=True, default=False)),
                ('code', models.IntegerField(blank=True, default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
