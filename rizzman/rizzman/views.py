from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Risk, Department
from django.contrib import messages
from .forms import CustomAuthenticationForm, UserProfileForm, RiskForm
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

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

def RiskListView(request):
    # Query awal
    user_priority = request.user.profile.jabatan.priority  # Ambil nilai priority user
    queryset = Risk.objects.filter(tingkat__gte=user_priority)
    # Search functionality
    search_query = request.GET.get('q', '').strip()
    if search_query:
        queryset = queryset.filter(
            Q(kode_resiko__icontains=search_query) |
            Q(tujuan__icontains=search_query) |
            Q(departemen__name__icontains=search_query)
        )

    # Filtering options
    departemen = request.GET.get('departemen')
    if departemen:
        queryset = queryset.filter(departemen__name=departemen)
    
    # Filtering tingkat
    selected_tingkat = request.GET.get('tingkat')
    if selected_tingkat:
        queryset = queryset.filter(tingkat=selected_tingkat)

    # Filter by risk level
    risk_level = request.GET.get('risk_level')
    if risk_level == 'high':
        queryset = queryset.filter(inherent_score__gt=15)
    elif risk_level == 'medium':
        queryset = queryset.filter(inherent_score__range=(8, 15))
    elif risk_level == 'low':
        queryset = queryset.filter(inherent_score__lt=8)

    # Sorting
    sort_by = request.GET.get('sort', '-created')
    queryset = queryset.order_by(sort_by)

    # Pagination
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Context data
    context = {
        'risks': page_obj,
        'departments': Department.objects.all(),
        'tingkat_options': Risk.objects.filter(tingkat__gte=user_priority).values_list('tingkat', flat=True).distinct(), # Ambil priority untuk filter
        'search_query': search_query,
        'selected_departemen': departemen,
        'selected_risk_level': risk_level,
        'selected_sort': sort_by,
        'total_risks': queryset.count(),
        'high_risk_count': queryset.filter(inherent_score__gt=15).count(),
        'medium_risk_count': queryset.filter(inherent_score__range=(8, 15)).count(),
        'low_risk_count': queryset.filter(inherent_score__lt=8).count(),
        'selected_tingkat': selected_tingkat,
    }

    return render(request, 'risk_list.html', context)


    
def risk_detail(request, id):
    try:
        # Ensure the user can only view their own risks
        risk = get_object_or_404(Risk, id=id)
        
        context = {
            'risk': risk,
            # Add any additional context data if needed
            'title': f'Detail Risiko - {risk.kode_resiko}',
        }
        
        return render(request, 'detail_resiko.html', context)
    
    except Risk.DoesNotExist:
        # If the risk doesn't exist or doesn't belong to the user
        raise Http404("Risk does not exist or you do not have permission to view it")