from django.urls import path

from twitteruser import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('twitteruser/<int:id>/', views.Profilepage.as_view(), name='profilepage'),
    path('follow/<int:id>/', views.Follow.as_view()),
    path('unfollow/<int:id>/', views.unfollow),
    path('notifcount/', views.notif_count),
]
