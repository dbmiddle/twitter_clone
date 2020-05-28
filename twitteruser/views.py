from django.shortcuts import render

from twitteruser.models import MyUser
from tweet.models import Tweet

# Create your views here.


def index(request):
    tweet = Tweet.objects.all()
    tweet_author = request.user
    return render(request, 'index.html', {'tweet': tweet, 'tweet_author': tweet_author})


def profile_page(request, id):
    user = MyUser.objects.get(id=id)
    return render(request, 'profile_page.html', {'user': user})
