from django.shortcuts import render

def index(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'index.html',context)

def login(request):
    context = {
        'title' : 'RizzMan'
    }
    return render(request,'login.html',context)