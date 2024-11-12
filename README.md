# Panduan Instalasi Aplikasi Web RizzMan

Panduan ini berisi instruksi langkah demi langkah untuk mengatur aplikasi web RizzMan, baik untuk pengaturan awal maupun untuk kolaborator.

## Instalasi Awal

### Persyaratan Sistem
- Git
- Python 3.x
- Node.js dan npm
- Laragon dengan Apache
- PostgreSQL

### Langkah 1: Mengunduh Repository
```bash
git clone https://github.com/ArbathAbdurrahman/RizzMan.git
cd RizzMan
```

### Langkah 2: Membuat Virtual Environment
Untuk Windows:
```bash
python -m venv venv
```

Untuk Linux/Mac:
```bash
python3 -m venv venv
```

### Langkah 3: Mengaktifkan Virtual Environment
Untuk Windows buka powershell:
```bash
.\venv\Scripts\activate.ps1
```

Untuk Linux/Mac:
```bash
source venv/bin/activate
```

### Langkah 4: Menginstal Requirements
```bash
cd rizzman
pip install -r requirements.txt
```

### Langkah 5: Pengaturan Database
1. Jalankan Laragon dan aktifkan Apache
2. Buat database PostgreSQL dengan kredensial berikut:
   - Username: postgres
   - Password: admin123
   - Database: db_rizzman
   - Port: 5432

### Langkah 6: Menjalankan Migrasi
```bash
python manage.py migrate
```

### Langkah 7: Membuat Superuser Django
```bash
python manage.py createsuperuser
```
Ikuti petunjuk untuk membuat akun admin.

### Langkah 8: Menjalankan Server Development
```bash
python manage.py runserver
```
Aplikasi sekarang dapat diakses di `http://localhost:8000`

### Langkah 9: Pengembangan Frontend
Saat mengerjakan pengembangan frontend, jalankan:
```bash
npm run build
```

## Panduan untuk Kolaborator

### Aturan Pengelolaan Branch

1. **Mengambil Perubahan Terbaru**
   - Untuk pengembangan frontend:
     ```bash
     git checkout front-end
     git pull origin front-end
     ```
   - Untuk pengembangan backend:
     ```bash
     git checkout back-end
     git pull origin back-end
     ```

2. **Mengirim Perubahan**
   ```bash
   git add .
   git commit -m "Pesan commit Anda"
   git push origin <nama-branch>  # front-end atau back-end
   ```

### Catatan Penting
- ⚠️ DILARANG push langsung ke branch `main`
- ⚠️ DILARANG melakukan merge branch tanpa izin
- Selalu bekerja pada branch yang ditentukan (`front-end` atau `back-end`)
- Lakukan pull secara rutin untuk mendapatkan kode terbaru

## Penyelesaian Masalah

Jika mengalami masalah selama instalasi, silakan periksa:
1. Pastikan semua persyaratan sistem sudah terinstal dengan benar
2. Periksa apakah virtual environment sudah aktif
3. Verifikasi kredensial database
4. Pastikan semua port yang diperlukan tersedia

## Dukungan

Untuk bantuan tambahan atau pertanyaan, silakan buat issue di repository GitHub.
