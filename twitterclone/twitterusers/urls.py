from django.contrib import admin
from django.urls import path
from twitterclone.twitterusers import views



urlpatterns = [
    path('signup/', views.new_user_view, name='signup'),
    path('follow/<str:username>/', views.follow_view, name='follow'),
    path('unfollow/<str:username>/', views.unfollow_view, name='unfollow'),
    path('profile/<str:username>/', views.profile_view, name="profile")

]