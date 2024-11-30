from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from django.contrib import messages
from .forms import CustomAuthenticationForm

def index(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'index.html',context)

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('/profile')  # Ganti '/profile' dengan URL tujuan setelah login
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def profile(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'profile.html',context)

def forms(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'forms.html',context)
def tabel(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'tabel.html',context)

def logout_view(request):
    logout(request)
    return redirect('/login/')