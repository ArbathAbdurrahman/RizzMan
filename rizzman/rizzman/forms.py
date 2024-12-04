from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile, Risk, Department, Bisnis, Kelompok

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'required': True,
        }),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'required': True,
        }),
        label="Password"
    )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['foto','nama', 'alamat', 'tanggal_lahir',]
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'BoxPlchdr cursor-not-allowed','readonly': 'readonly',}),
            'alamat': forms.TextInput(attrs={'class': 'BoxPlchdr cursor-not-allowed','readonly': 'readonly',}),
            'tanggal_lahir': forms.DateInput(attrs={
                'class': 'BoxPlchdr cursor-not-allowed remove-arrow',
                'readonly': 'readonly',
                
                'type': 'date',  # Pastikan type adalah 'date' untuk mendukung input kalender
            }),
        }

# Risk Forms
class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = [
            'tujuan', 
            'proses_bisnis', 
            'kelompok_resiko', 
            'kode_resiko', 
            'uraian_peristiwa', 
            'penyebab_resiko', 
            'sumber_resiko', 
            'akibat', 
            'akibat_finansial', 
            'departemen',
            'pemilik_resiko',
            'inherent_likelihood', 
            'inherent_impact', 
            'control', 
            'memadai', 
            'status', 
            'residual_likelihood', 
            'residual_impact', 
            'perlakuan', 
            'tindakan_mitigasi', 
            'mitigasi_likelihood', 
            'mitigasi_impact',
        ]

        widgets = {
                'tujuan': forms.TextInput(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'proses_bisnis': forms.Select(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'kelompok_resiko': forms.Select(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'kode_resiko': forms.TextInput(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'uraian_peristiwa': forms.Textarea(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                    'rows': 3
                }),
                'penyebab_resiko': forms.Textarea(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                    'rows': 3
                }),
                'sumber_resiko': forms.Select(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'akibat': forms.Textarea(attrs={
                    'class': 'bg-slate-100 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                    'rows': 3
                }),
                'akibat_finansial': forms.NumberInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'pemilik_resiko': forms.TextInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'departemen': forms.Select(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'inherent_likelihood': forms.NumberInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'inherent_impact': forms.NumberInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'control': forms.Select(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'memadai': forms.Select(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'status': forms.Select(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'residual_likelihood': forms.NumberInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'residual_impact': forms.NumberInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'perlakuan': forms.Select(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'tindakan_mitigasi': forms.Textarea(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500',
                    'rows': 3
                }),
                'mitigasi_likelihood': forms.NumberInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                }),
                'mitigasi_impact': forms.NumberInput(attrs={
                    'class': 'block bg-slate-100 w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
                })
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Semua harus diisi
        for field_name in self.fields:
            self.fields[field_name].required = True
            
        # Setup katogori dinamis
        self.fields['departemen'].queryset = Department.objects.all()
        self.fields['proses_bisnis'].queryset = Bisnis.objects.all()
        self.fields['kelompok_resiko'].queryset = Kelompok.objects.all()
        
        # Handling eror
        for field in self.fields:
            self.fields[field].error_messages = {
                'required': f'{field.replace("_", " ").title()} harus diisi.',
                'invalid': f'Masukkan {field.replace("_", " ")} yang valid.'
            }

    def clean(self):
        cleaned_data = super().clean()
        
        # Validasi numerik
        numeric_fields = [
            'inherent_likelihood', 'inherent_impact', 
            'residual_likelihood', 'residual_impact', 
            'mitigasi_likelihood', 'mitigasi_impact',
            'akibat_finansial'
        ]
        
        for field in numeric_fields:
            value = cleaned_data.get(field)
            if value is None:
                self.add_error(field, f'{field.replace("_", " ").title()} harus diisi.')
            elif not isinstance(value, (int, float)):
                self.add_error(field, f'{field.replace("_", " ").title()} harus berupa angka.')
            
        # Validasi maksimal
        if cleaned_data.get('inherent_likelihood', 0) > 5:
            self.add_error('inherent_likelihood', 'Likelihood maksimal 5')
        
        if cleaned_data.get('inherent_impact', 0) > 5:
            self.add_error('inherent_impact', 'Impact maksimal 5')

        if cleaned_data.get('residual_likelihood', 0) > 5:
            self.add_error('residual_likelihood', 'Likelihood maksimal 5')
        if cleaned_data.get('residual_impact', 0) > 5:
            self.add_error('residual_impact', 'Impact maksimal 5')

        if cleaned_data.get('mitigasi_likelihood', 0) > 5:
            self.add_error('mitigasi_likelihood', 'Likelihood maksimal 5')
        if cleaned_data.get('mitigasi_impact', 0) > 5:
            self.add_error('mitigasi_impact', 'Impact maksimal 5')
        
        return cleaned_data

    def clean_kode_resiko(self):
        kode_resiko = self.cleaned_data.get('kode_resiko')
        
        if not kode_resiko:
            raise forms.ValidationError("Kode Resiko harus diisi.")
        
        # Kode resiko unik
        if Risk.objects.filter(kode_resiko=kode_resiko).exists():
            raise forms.ValidationError("Kode Resiko sudah ada. Gunakan kode yang unik.")
        
        return kode_resiko

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Hitung score
        instance.inherent_score = (
            instance.inherent_likelihood * 
            instance.inherent_impact
        )
        instance.residual_score = (
            instance.residual_likelihood * 
            instance.residual_impact
        )
        instance.mitigasi_score = (
            instance.mitigasi_likelihood * 
            instance.mitigasi_impact
        )
        
        if commit:
            instance.save()
        return instance
