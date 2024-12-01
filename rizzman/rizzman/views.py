from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Risk
from django.contrib import messages
from .forms import CustomAuthenticationForm, UserProfileForm, RiskForm

def index(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Anda berhasil login")
                return redirect('/profile')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = CustomAuthenticationForm()

    context = {
        'title' : 'RizzMan',
        'form' : form,
    }
    return render(request,'index.html',context)

@login_required
def profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES, instance=user_profile)
        
        # Proses form data profil
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect ke halaman profil

    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'user_profile': user_profile,
        'form': form,
    }
    return render(request, 'profile.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def tabel(request):
    tabel = Risk.objects.filter(user = request.user)
    context = {
        'title' : 'RizzMan',
        'tabel' : tabel
    }
    return render(request,'tabel.html',context)

@login_required
def edit_risk(request, id):
    # Ambil instance dari objek Risk yang akan diedit
    risk = get_object_or_404(Risk, id=id)

    # Validasi untuk hak akses
    if request.user != risk.user:
        messages.error(request, "Kamu tidak mempunyai hak untuk mengedit ini.")
        return redirect('tabel')
    
    if request.method == "POST":
        form = RiskForm(request.POST, instance=risk)  # Instance untuk binding data
        if form.is_valid():
            form.save()
            messages.success(request,"Resiko berhasil diperbarui.")
            return redirect('tabel')  # Redirect setelah berhasil
    else:
        form = RiskForm(instance=risk)  # Prepopulate dengan data dari instance
        
    return render(request, 'forms.html', {'form': form})

@login_required
def delete_risk(request, id):
    risk = get_object_or_404(Risk, id=id)

    # Validasi untuk hak akses
    if request.user != risk.user:
        messages.error(request, "Kamu tidak mempunyai hak untuk menghapus ini.")
        return redirect('tabel')
    else:
        # Hapus risiko
        profil = get_object_or_404(UserProfile, user=request.user)
        profil.total_pengisian -= 1
        profil.save()
        risk.delete()
        messages.success(request, "Resiko berhasil dihapus.")
        return redirect('tabel')


@login_required
def create_risk(request):
    """
    View for creating a new risk entry
    """
    if request.method == 'POST':
        form = RiskForm(request.POST)
        if form.is_valid():
            risk = form.save(commit=False)
            risk.user = request.user
            risk.save()

            profil = get_object_or_404(UserProfile, user=request.user)
            profil.total_pengisian += 1
            profil.save()

            messages.success(request, 'Risiko berhasil dibuat!')
            return redirect('tabel')  # Redirect to a list view of risks
    else:
        form = RiskForm()
    
    return render(request, 'forms.html', {
        'form': form,
        'title': 'Buat Risiko Baru'
    })

@login_required
def risk_detail(request, risk_id):
    """
    View for showing details of a specific risk
    """
    try:
        risk = Risk.objects.get(id=risk_id)
    except Risk.DoesNotExist:
        messages.error(request, 'Risiko tidak ditemukan.')
        return redirect('risk_list')
    
    return render(request, 'risk_detail.html', {
        'risk': risk,
        'title': f'Detail Risiko {risk.kode_resiko}'
    })