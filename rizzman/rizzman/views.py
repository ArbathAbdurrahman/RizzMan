from django.shortcuts import render

def index(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'index.html',context)

def profile(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'profile.html',context)

def signup(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'signup.html',context)

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