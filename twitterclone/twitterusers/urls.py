from django.contrib import admin
from django.urls import path
from twitterclone.twitterusers import views




urlpatterns = [
    path('signup/', views.NewUserView.as_view(), name='signup'),
    path('follow/<str:username>/', views.FollowView.as_view(), name='follow'),
    path('unfollow/<str:username>/', views.UnfollowView.as_view(), name='unfollow'),
    path('profile/<str:username>/', views.ProfileView.as_view(), name="profile")

]