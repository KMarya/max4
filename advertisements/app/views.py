from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def go_back(request):
    return render(request, 'go back.html')

def top_sellers(request):
    return render(request, 'top_sellers.html')

def advertisement(request):
    return render(request, 'advertisement.html')

def advertisement_post(request):
    return render(request, 'advertisement-post.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')