from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.loginview),
    path('logout/', views.logoutview),
    path('signup/', views.signup),
]
