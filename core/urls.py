from importlib.resources import path
from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('settings', views.Settings, name="settings"),
    path('upload', views.Upload, name="upload"),
    path('follow', views.follow, name="follow"),
    path('search', views.search, name="search"),
    path('profile/<str:pk>', views.profile, name="profile"),
    path('like-post', views.like_post, name="like-post"),
    path('signup', views.Signup, name="signup"),
    path('', views.Signin, name="signin"),
    path('logout', views.Logout, name="logout"),
]