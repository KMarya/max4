from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from django.urls import reverse, reverse_lazy
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app/index.html', context)

def top_sellers(request):
    return render(request, 'app/top_sellers.html')

def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'advertisement': advertisement}
    return render(request, 'app/advertisement.html', context)

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
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