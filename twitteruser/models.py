from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):
    user_name = models.CharField(max_length=50, null=True, blank=True)
    followingg = models.ManyToManyField('self', related_name='following', symmetrical=False)
