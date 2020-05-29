from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect

from twitteruser.models import MyUser
from tweet.models import Tweet

# Create your views here.


@login_required
def index(request):
    tweetdetail = Tweet.objects.all()
    return render(request, 'index.html', {'tweetdetail': tweetdetail})


def profile_page(request, id):
    otheruser = MyUser.objects.get(id=id)
    tweetdetail = Tweet.objects.filter(tweet_author=otheruser)
    return render(request, 'profile_page.html', {'otheruser': otheruser, 'tweetdetail': tweetdetail})


def follow(request, id):
    user_to_follow = MyUser.objects.get(id=id)
    current_user = MyUser.objects.get(id=request.user.id)
    current_user.following.add(user_to_follow)
    return HttpResponseRedirect(reverse('profilepage'))


def unfollow(request, id):
    user_to_unfollow = MyUser.objects.get(id=id)
    current_user = MyUser.objects.get(id=request.user.id)
    current_user.following.remove(user_to_unfollow)
    return HttpResponseRedirect(reverse('profilepage'))
