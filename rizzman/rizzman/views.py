from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import UserProfile, Risk
import pytz
from datetime import datetime
import hashlib
import json
from django.core.serializers.json import DjangoJSONEncoder


timezone = pytz.timezone("Asia/Jakarta")

def alert(kalimat):
    return "<script> alert('{}'); </script>".format(kalimat)

def redirect(url):
    return "<script> location.href='{}' </script>".format(url)

def index(request):
    context = {
        'title' : 'RizzMan'
    }
    if 'user' not in request.session:
        return HttpResponse(alert("Kamu belum login!")+redirect("/login/"))


    return HttpResponseRedirect("/profile/")

def edit(request):
    if request.method != "PUT":
        response = render(request,'403.html')
        response.status_code=403
        return response

    usernaem 

def create_user(request):
    context = {'title':'RizzMan'}
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
    context = {'title' : 'RizzMan'}
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
    context={'title':'RizzMan','error':0};
    if 'user' in request.session:
        return HttpResponse(alert("Anda sudah login") + redirect("/"));
    if request.method != "POST":
        return render(request,'login.html',context)

    username = request.POST.get('email')
    password = request.POST.get('password')
    user = UserProfile.objects.filter(user=username).values()
    if len(user) == 1:
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if (password_hash != user[0]['password']):
            context['error'] = 1
            context['error_message'] = "Password atau username anda salah, mohon cek kembali!"
            return render(request,"login.html",context=context)
        else:
            request.session['user']=username
            request.session['logged']=True
            return HttpResponse(alert("Password anda benar")+redirect("/"))
    else:
        context['error'] = 1
        context['error_message'] = "Password atau username anda salah, mohon cek kembali!"
        return render(request,"login.html",context=context)

def get_rgb(t):
    return "{},{},{}".format((255*t)/1000,0,255-(255*t/1000))
 
def chart(request):
    queryset = Risk.objects.all().values()
    datapoints = [{'x':1,'y':-1000,'r':10}]
    labels = []
    colors = []
    for i in range(len(queryset)):
        datapoint = {}
        datapoint['x'] = i+1
        datapoint['y'] = queryset[i]['inherent_score']
        datapoint['label'] = queryset[i]['kode_resiko']
        datapoint['r'] = 50
        datapoint['backgroundColor'] = 'rgb(0,0,0)'
        datapoints.append(datapoint)
        labels.append(queryset[i]['kode_resiko'])
        color = "rgb({})".format(get_rgb(datapoint['y']))
        colors.append(color)

    datapoints_json = json.dumps(datapoints,cls=DjangoJSONEncoder)
    return render(request,'chart.html',{'datapoints':datapoints_json,'labels':labels,'colors':colors})



def forms(request):
    context = {'title':'RizzMan'}

    if 'user' not in request.session:
        response = render(request,'403.html',context)
        response.status_code=403
        return response


    if request.method != "POST":
        return render(request,'forms.html',context)

    user = request.session['user']
    tujuan = request.POST.get('tujuan')
    proses_bisnis = request.POST.get('proses_bisnis')
    kelompok_resiko = request.POST.get('kelompok_resiko')
    sumber_resiko = str(request.POST.get('sumber_resiko')) == 'Internal'
    akibat = request.POST.get('akibat')
    akibat_finansial = request.POST.get('akibat_finansial')
    pemilik_resiko = request.POST.get('pemilik_resiko')
    departemen  = request.POST.get('departemen')
    inherent_likelihood = request.POST.get('inherent_likelihood')
    inherent_impact = request.POST.get('inherent_impact')
    inherent_score = request.POST.get('inherent_score')
    control = str(request.POST.get('control')) == 'Ada'
    memadai = str(request.POST.get('memadai')) == 'Ya'
    residual_likelihood = request.POST.get('residual_likelihood')
    residual_impact = request.POST.get('residual_impact')
    residual_score = request.POST.get('residual_score')
    perlakuan = str(request.POST.get('perlakuan')) == 'Accept'
    tindakan_mitigasi = request.POST.get('tindakan_mitigasi')
    mitigasi_likelihood = request.POST.get('mitigasi_likelihood')
    mitigasi_impact = request.POST.get('mitigasi_impact')
    mitigasi_score = request.POST.get('mitigasi_score')
    kode_resiko = request.POST.get('kode_resiko')
    penyebab_resiko = request.POST.get('penyebab_resiko')

    status = request.POST.get('')
    status_code = status == 'Dijalankan'

    _Risk = Risk.objects.filter(kode_resiko=kode_resiko).values()
    created = datetime.now(timezone)
    total_modifikasi = 0

    _Risk = Risk(user=user,tujuan=tujuan,proses_bisnis=proses_bisnis,
        kelompok_resiko=kelompok_resiko,kode_resiko=kode_resiko,
        penyebab_resiko=penyebab_resiko,sumber_resiko=sumber_resiko,
        akibat=akibat,akibat_finansial=akibat_finansial,pemilik_resiko=pemilik_resiko,
        departemen=departemen,inherent_likelihood=inherent_likelihood,inherent_impact=inherent_impact,
        control=control,memadai=memadai,status=status_code,residual_likelihood=residual_likelihood,
        residual_impact=residual_impact,perlakuan=perlakuan,tindakan_mitigasi=tindakan_mitigasi,
        mitigasi_likelihood=mitigasi_likelihood,mitigasi_impact=mitigasi_impact,inherent_score=(int(inherent_likelihood) * int(inherent_impact)),
        residual_score=(int(residual_likelihood) * int(residual_impact)),mitigasi_score=(int(mitigasi_likelihood) * int(mitigasi_impact))
    )
    _Risk.save()
    return HttpResponse(alert("Berhasil dimasukkan!")+redirect("/tabel/"))

def signup(request):
    context = {'title' : 'RizzMan'}
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        nama = request.POST.get('nama')
        jabatan = request.POST.get("jabatan")
        nomor_induk = request.POST.get('NomorInduk')
        alamat = request.POST.get('alamat')
        tanggal_lahir = request.POST.get('tanggalLahir')
        gelar = request.POST.get('gelar')
        
        email_check = UserProfile.objects.filter(user=email).values()
        if len(email_check) > 0:
            return HttpResponse(alert("Email sudah digunakan!")+redirect("/signup/"))
        password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        _UserProfile= UserProfile(user=email,password=password_hash,namalengkap=nama,jabatan=jabatan,gelar=gelar,nomor_induk=nomor_induk,alamat=alamat,tanggal_lahir=tanggal_lahir)
        _UserProfile.save()
        return HttpResponse(alert("Berhasil! silahkan login kembali!")+redirect("/login/"))

    else:
        return render(request,'signup.html',context)

def tabel(request):
    context = {'title':'RizzMan'}
    if 'user' not in request.session:
        response = HttpResponse("<h1> Login dulu! </h1>")
        response.status_code=403
        return response
    _Risk = Risk.objects.filter(user=request.session['user']).values
    context['risks'] = _Risk
    return render(request,'tabel.html',context)

def profile(request):
    context = {'title':'RizzMan'}
    username = request.session['user']
    user_profile = UserProfile.objects.filter(user=username).values()
    if 'user' not  in request.session:
        response = HttpResponse("<h1> Login dulu! </h1><a href='/login/'> Silahkan klik link ini </a>")
        response.status_code=403
        return response
    else:
        context.update(user_profile[0])
        return render(request,'profile.html',context)

def home(request):
    context = {'title' : 'Home'}
    return render(request,'home.html',context)

def handler404(request,exception):
    response = render(request,"404.html")
    response.status_code=404
    return response

def handler403(request,exception):
    response = render(request,"403.html")
    response.status_code=403
    return response