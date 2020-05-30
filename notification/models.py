from django.db import models
from twitteruser.models import MyUser
from tweet.models import Tweet

# Create your models here.


class Notification(models.Model):
    receiving_user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    viewed = models.BooleanField(default=False)