from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.detail import DetailView

from twitteruser.models import MyUser
from tweet.models import Tweet
from notification.models import Notification

# Create your views here.


@login_required
def index(request):
    tweetdetail = Tweet.objects.all()
    tweetcount = Tweet.objects.filter(tweet_author=request.user)
    return render(request, 'index.html', {'tweetdetail': tweetdetail, 'tweetcount': tweetcount})


# class-based view conversion
class Profilepage(DetailView):
    model = MyUser
    context_object_name = 'otheruser'

    def get(self, request, id):
        otheruser = MyUser.objects.get(id=id)
        tweetdetail = Tweet.objects.filter(tweet_author=otheruser)
        tweetcount = Tweet.objects.filter(tweet_author=request.user)
        return render(request, 'profile_page.html', {'otheruser': otheruser, 'tweetdetail': tweetdetail, 'tweetcount': tweetcount})


# class-based view conversion
class Follow(DetailView):

    def get(self, request, id):
        user_to_follow = MyUser.objects.get(id=id)
        current_user = MyUser.objects.get(id=request.user.id)
        current_user.followingg.add(user_to_follow)
        current_user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def unfollow(request, id):
    user_to_unfollow = MyUser.objects.get(id=id)
    current_user = MyUser.objects.get(id=request.user.id)
    current_user.followingg.remove(user_to_unfollow)
    current_user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def notif_count(request):
    current_user = MyUser.objects.get(username=request.user)
    notification = Notification.objects.filter(receiving_user=current_user)
    return render(request, 'navigation.html', {'notification': notification})
