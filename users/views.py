from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
# Create your views here.

# @never_cache
# def logout_view(request):
#     logout(request) #Log the user out
#     return render(request,, 'logout.html')



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

@login_required
def profile(request):
    return render(request, 'user/profile.html')

