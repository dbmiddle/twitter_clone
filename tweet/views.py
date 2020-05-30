from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect

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


def compose(request):
    html = 'compose_tweet_form.html'

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.tweet_author = MyUser.objects.get(id=request.user.id)
            tweet.save()
            notify_user(tweet)
        return HttpResponseRedirect(reverse('homepage'))
    notifications = Notification.objects.filter(receiving_user=request.user)
    form = TweetForm()

    return render(request, html, {'form': form, 'notifications': notifications})


def tweetdetail(request, tweetdetail_id):
    tweetdetail = Tweet.objects.get(id=tweetdetail_id)
    return render(request, 'tweetdetail.html', {'tweetdetail': tweetdetail})
