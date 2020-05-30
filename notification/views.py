from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from notification.models import Notification
from twitteruser.models import MyUser


# Create your views here.


@login_required
def notification(request):
    current_user = MyUser.objects.get(username=request.user)
    notification = Notification.objects.filter(receiving_user=current_user, viewed=False)
    for notif in notification:
        notif.viewed = True
        notif.save()
    return render(request, 'notification.html', {'notification': notification})
