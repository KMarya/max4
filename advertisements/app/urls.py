from django.urls import path, include
from django.contrib import admin
from .views import index, top_sellers, advertisement_detail, advertisement_post, login, profile, register

urlpatterns = [
    path('', index, name='index'),
    path('top_sellers.html', top_sellers, name='top_sellers'),
    path('advertisement.html', advertisement_detail, name='advertisement'),
    path('advertisement-post.html', advertisement_post, name='advertisement-post'),
    path('login.html', login, name='login'),
    path('profile.html', profile, name='profile'),
    path('register.html', register, name='register'),
]
