# Generated by Django 3.2.7 on 2021-09-16 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0003_serverinformation_serverinformation_15m_serverinformation_1h_serverinformation_24h_serverinformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ServerInformation',
        ),
        migrations.DeleteModel(
            name='ServerInformation_15m',
        ),
        migrations.DeleteModel(
            name='ServerInformation_1h',
        ),
        migrations.DeleteModel(
            name='ServerInformation_24h',
        ),
        migrations.DeleteModel(
            name='ServerInformation_30m',
        ),
        migrations.DeleteModel(
            name='ServerInformation_6h',
        ),
    ]