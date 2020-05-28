from django.urls import path

from twitteruser import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('twitteruser/<int:id>/', views.profile_page),
]
