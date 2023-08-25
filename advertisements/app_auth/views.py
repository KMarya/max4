from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect_url
        else:
            return request, 'app_auth/login.html'
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect_url
    return request, 'app_auth/login.html', {'error': '404 User not found'}

def profile_view(request):
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    logout(request)
    return render(reverse('login'))