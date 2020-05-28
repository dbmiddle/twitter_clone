from django.urls import path

from tweet import views

urlpatterns = [
    path('compose/', views.compose, name='composepage'),
    path('tweet/<int:tweetdetail_id>/', views.tweetdetail),
]
