# Generated by Django 3.0.6 on 2020-05-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=140),
        ),
    ]