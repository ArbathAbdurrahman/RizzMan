from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import UserProfile
import hashlib

def alert(kalimat):
    return "<script> alert('{}'); </script>".format(kalimat)

def redirect(url):
    return "<script> location.href='{}' </script>".format(url)

def index(request):
    context = {
        'title' : 'RizzMan'
    }

    return render(request,'login.html',context)

def create_user(request):
    context = {}
    if request.method != "POST":
        return render(request,"signup.html")
    username = request.POST.get('email');
    password = request.POST.get('password')

    user = UserProfile.objects.filter(user=username).values()
    if len(user) > 0:
        return HttpResponse("Email sudah ada!")
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user_added = UserProfile(user=username,password=password_hash,nomor_induk="",jabatan="",gelar="",alamat="",tanggal_lahir="2000-01-01",foto="",total_pengisian=0)
    user_added.save()
    return HttpResponse("User telah dibuat!")

def insert_data(request):
    if request.method != "POST":
        return render(request,"")

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        del request.session['logged']
        return HttpResponse(alert("Berhasil Log Out!")+redirect("/login/"))
    else:
        return HttpResponse(alert("Kamu belum masuk!")+redirect("/login/"))

def login(request):
    context={};
    if 'user' in request.session:
        return HttpResponse(alert("Anda sudah login") + redirect("/beranda/"));
    if request.method != "POST":
        return render(request,'login.html',context);

    username = request.POST.get('email')
    password = request.POST.get('password')
    user = UserProfile.objects.filter(user=username).values()
    if len(user) == 1:
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if (password_hash != user[0]['password']):
            return HttpResponse(alert("Password anda salah"));
        else:
            request.session['user']=username
            request.session['logged']=True
            return HttpResponse(alert("Password anda salah")+redirect("/login/"))
    else:
        return HttpResponse(alert("Password anda salah")+redirect("/login/"))

def home(request):
    if 'username'  not in request.session:
        return HttpResponse("Gak bisa!!")
    else:
        return HttpResponse("Bisa!!")
