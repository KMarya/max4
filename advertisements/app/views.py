from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from django.urls import reverse
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app/index.html', context)

def top_sellers(request):
    return render(request, 'app/top_sellers.html')

def advertisement(request):
    return render(request, 'app/advertisement.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('index')
            return redirect(url)
    else:
        form = AdvertisementForm()

    context = {'form': form}
    return render(request, 'app/advertisement-post.html', context)

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')

def register(request):
    return render(request, 'app_auth/register.html')