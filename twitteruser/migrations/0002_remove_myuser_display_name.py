# Generated by Django 3.0.6 on 2020-05-28 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='display_name',
        ),
    ]