from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from .models import LoginAttempt
# Create your views here.

# @never_cache
# def logout_view(request):
#     logout(request) #Log the user out
#     return render(request,, 'logout.html')
max_try = 3
lock_time = 15  # in minutes



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account is created!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})

# def logout(request):
#     return render(request, 'user/logout.html')

def login(request):
    from django.contrib.auth import authenticate
    from .forms import LoginForm
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            loginAttempt = LoginAttempt.objects.get_or_create(user=User.objects.get(username=username))
            if not loginAttempt[0].is_locked():
                if not loginAttempt[0].failed_attempts >= max_try:
                    if user is not None:
                        from django.contrib.auth import login as auth_login
                        auth_login(request, user)
                        loginAttempt[0].reset()
                        return redirect('food:index')
                    else:
                        loginAttempt[0].increment()
                        messages.error(request, 'Invalid credentials. Please try again.')
                else:
                    loginAttempt[0].lock_for(minutes=lock_time)
                    messages.error(request, 'Your account is locked due to multiple failed login attempts. Please try again after 15 minutes.')
                    return render(request, 'user/login.html', {'form': form})
            else:
                messages.error(request, 'Your account is locked due to multiple failed login attempts. Please try again later.')
                return render(request, 'user/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

