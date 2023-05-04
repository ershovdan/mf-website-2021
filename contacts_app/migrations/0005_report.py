# Generated by Django 3.1.3 on 2021-03-03 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts_app', '0004_delete_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('text', models.TextField(unique=True)),
                ('is_report', models.BooleanField()),
            ],
        ),
    ]