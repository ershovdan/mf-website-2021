# Generated by Django 3.1.3 on 2021-03-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0023_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='bug_type',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='title',
            field=models.CharField(blank=True, max_length=200, unique=True),
        ),
    ]
