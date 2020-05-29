from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect

from tweet.forms import TweetForm
from tweet.models import Tweet
from twitteruser.models import MyUser

# Create your views here.


def compose(request):
    html = 'compose_tweet_form.html'

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.tweet_author = MyUser.objects.get(id=request.user.id)
            tweet.save()

        return HttpResponseRedirect(reverse('homepage'))
    form = TweetForm()

    return render(request, html, {'form': form})


def tweetdetail(request, tweetdetail_id):
    tweetdetail = Tweet.objects.get(id=tweetdetail_id)
    # tweet_author = MyUser.objects.all()
    return render(request, 'tweetdetail.html', {'tweetdetail': tweetdetail})
