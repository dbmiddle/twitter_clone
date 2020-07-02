from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.views.generic.detail import View
from django.views.generic.detail import DetailView

from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import MyUser
from notification.models import Notification

import re

# Create your views here.


def notify_user(tweet):
    at_user_patten = r'([@#][\w_-]+)'
    tag = re.match(at_user_patten, tweet.body)
    if tag:
        notified_user = MyUser.objects.get(username=tag.group()[1:])
        Notification.objects.create(
            receiving_user=notified_user,
            tweet=tweet
        )


# class-based view form conversion
class Compose(View):

    def post(self, request, *args, **kwargs):
        form = TweetForm(request.POST)
        tweet = form.save(commit=False)
        tweet.tweet_author = MyUser.objects.get(id=request.user.id)
        tweet.save()
        notify_user(tweet)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(receiving_user=request.user)
        form = TweetForm()
        return render(request, 'compose_tweet_form.html', {'form': form, 'notifications': notifications})


# class-based view conversion
class Tweetdetail(DetailView):
    model = Tweet
    context_object_name = 'tweetdetail'

    def get(self, request, tweetdetail_id):
        tweetdetail = Tweet.objects.get(id=tweetdetail_id)
        return render(request, 'tweetdetail.html', {'tweetdetail': tweetdetail})
