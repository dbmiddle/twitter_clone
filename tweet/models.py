from django.db import models
from django.utils import timezone

from twitteruser.models import MyUser


# Create your models here.


class Tweet(models.Model):
    body = models.TextField(max_length=140)
    tweet_author = models.ForeignKey(
        MyUser,
        related_name='tweet_author',
        blank=True, on_delete=models.CASCADE,
        null=True)
    date = models.DateTimeField(default=timezone.now)
