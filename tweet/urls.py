from django.urls import path

from tweet import views

urlpatterns = [
    path('compose/', views.Compose.as_view(), name='composepage'),
    path('tweet/<int:tweetdetail_id>/', views.Tweetdetail.as_view(), name='tweetdetail'),
]
