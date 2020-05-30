from django.urls import path

from twitteruser import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('twitteruser/<int:id>/', views.profile_page, name='profilepage'),
    path('follow/<int:id>/', views.follow),
    path('unfollow/<int:id>/', views.unfollow),
    path('notifcount/', views.notif_count),
]
