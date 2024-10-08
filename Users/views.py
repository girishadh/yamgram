from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        form = UserRegisterForm
    return render(request, 'users/register.html', {'form':form})

def profile(request):

    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email

        context = {
            'username' : username,
            'email' : email
        }

        return render(request, 'Users/profile.html', context)
    else:
        return redirect('login')