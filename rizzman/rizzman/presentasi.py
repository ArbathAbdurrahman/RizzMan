Pembahsan = {
    'OOP' : 'paradigma pemrograman yang mengorganisir kode ke dalam objek, yang merupakan instance dari kelas',
    'Encapsulation' : 'konsep menyembunyikan detail internal dan membatasi akses langsung ke atribut dan metode',
    'Constructor' : 'metode khusus yang dipanggil saat objek dibuat',
}







# 15

# from .models import Risk, Bisnis
# from django import forms

# class RiskForm(forms.ModelForm): # kelas RiskForm adalah turunan dari forms.ModelForm
#     class Meta: # mengenkapsulasi konfigurasi model menggunakan inheritance (pewarisan) melalui class Meta
#         model = Risk # mengambil class model
#         fields = ['tujuan', 'prose_bisnis','dst'] # list berasal dari models.py

#         def __init__(self, *args, **kwargs): # membungkus logika inisialisasi form
#             #inisialisasi objek
#             super().__init__(*args, **kwargs) 
            
#             # Semua harus diisi
#             for field_name in self.fields:
#                 if field_name == 'status':
#                     self.fields[field_name].required = False
#                 else: 
#                     self.fields[field_name].required = True

#             self.fields['proses_bisnis'].queryset = Bisnis.objects.all()






# Jika tanpa Framework (50)
class RiskForm:
    def __init__(self):
        self._tujuan = None
        self.__proses_bisnis = None
        self._errors = {}

    # Getter untuk tujuan
    def get_tujuan(self):
        return self._tujuan

    # Setter untuk tujuan dengan validasi
    def set_tujuan(self, tujuan):
        if not tujuan:
            raise ValueError("Tujuan tidak boleh kosong")
        self._tujuan = tujuan

    # Getter untuk proses_bisnis
    def get_proses_bisnis(self):
        return self.__proses_bisnis

    # Setter untuk proses_bisnis dengan validasi
    def set_proses_bisnis(self, proses_bisnis):
        if proses_bisnis is None:
            raise ValueError("Proses bisnis harus dipilih")
        self.__proses_bisnis = proses_bisnis

    # Getter untuk errors
    def get_errors(self):
        return self._errors

    # Metode set_data yang menggunakan setter
    def set_data(self, tujuan=None, proses_bisnis=None):
        if tujuan is not None:
            self.set_tujuan(tujuan)
        
        if proses_bisnis is not None:
            self.set_proses_bisnis(proses_bisnis)

    def validate(self):
        self._errors.clear() # Bersihkan eror sebelumya

        # Validasi tipe
        if not isinstance(self._tujuan, str):
            self._errors['tujuan'] = 'Tujuan harus berupa teks'

        # Validasi proses bisnis
        if not self.__proses_bisnis:
            self._errors['proses_bisnis'] = 'Proses bisnis harus dipilih'

        return len(self._errors) == 0

# Contoh penggunaan
form = RiskForm() # Membuat instance baru dari kelas RiskForm
form.set_tujuan("Membina Mahasiswa")
form.set_proses_bisnis("Akademik")

if form.validate():
    print(f'Tujuan : {form._tujuan}') # Mengakses private 
    print(f'Bisnis : {form._RiskForm__proses_bisnis}') # Mengakses private ultimate
    print("Data valid")
else:
    print("Error :", form.get_errors())