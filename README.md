# Tasaki Shop: Misaka City's Best Football Merchandise
**URL**: https://arya-putra41-tasakishop.pbp.cs.ui.ac.id/

# Tugas 2
## 1: Jelaskan bagaimana Anda mengimplementasikan checklist di atas secara step-by-step

### Membuat sebuah proyek Django baru
Saya pertama menginisiasi folder lokal `tasaki-shop` dengan Git (`git init`). Kemudian, saya membuka *virtual environment* Python (`python -m venv env`, kemudian `env\Scripts\activate`), membuat berkas `requirements.txt` berisi nama-nama *dependency library* (termasuk Django itu sendiri, Gunicorn, dan Whitenoise), lalu menggunakan pip untuk menginstal semua *dependency* tersebut (`pip install requirements.txt`). Untuk membuka proyek Django, saya menggunakan perintah `django-admin startproject tasaki_shop .`.

Setelah membuka proyek, kita kemudian perlu mengatur *environment variable* dan mengatur opsi proyek di berkas `tasaki_shop/settings.py` untuk menggunakan variabel tersebut sekaligus mengatur *host* yang boleh menjalankan proyek kita.

### Membuat aplikasi bermama `main`
Untuk membuat aplikasi, kita menggunakan perintah `python manage.py startapp main` di folder `tasaki-shop`. Kemudian, kita mengedit `INSTALLED_APPS` pada `settings.py` untuk memasukkan `main` sebagai aplikasi yang dapat dijalankan oleh proyek `tasaki_shop`. 

### Membuat model Product
Model berupa kelas `Product` dimasukkan dalam berkas `main/models.py` dan berisi atribut seperti berikut:
- `name: CharField`
- `price: IntegerField`
- `description: CharField`
- `thumbnail: URLField`
- `category: CharField`
- `is_featured: BooleanField`
- Saya juga menambahkan atribut `stock: PositiveIntegerField`

### Membuat fungsi pada `views.py` dan membuat template
Di `views.py` saya membuat fungsi `show-main` yang memberikan variabel *context* berupa nama, NPM, dan kelas. Berikutnya saya membuat template `main.html` yang dapat diisi oleh variabel-variabel tersebut.

### Melakukan routing pada proyek
Hal ini dilakukan dengan berkas `urls.py` di `tasaki_shop` dan `urls.py` di `main`. Di `main`, kita mengonfigurasi path yang akan menjalankan fungsi `show-main` dari *views*, sedangkan di `tasaki_shop`, kita membuat path yang mengarah kepada berkas URL di main (`include('main.urls')`).
    
### Melakukan deployment ke PWS
Kita membuka proyek baru di PWS dengan nama `tasakishop`, mengatur *environment variable*, dan melakukan *deployment* melalui `git push pws master`.
  
## 2: Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`

Silakan lihat link Canva berikut: https://www.canva.com/design/DAGyGs5w1og/V8q60vdq0ojWWiEL_knnPg/view?utm_content=DAGyGs5w1og&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he395269a12

## 3: Jelaskan peran `settings.py` dalam proyek Django

Mengutip dari Django Software Foundation (2025), `settings.py` pada sebuah proyek Django (dalam hal ini `tasaki_shop`) berfungsi untuk melakukan konfigurasi-konfigurasi yang diperlukan dalam menjalankan proyek tersebut. Berikut adalah beberapa fungsi `settings.py` yang kritis atau berguna dalam menjalankan aplikasi web Django:
 - Mengatur web server yang terotorisasi menjalankan aplikasi kita melalui `ALLOWED_HOSTS`
 - Mengatur koneksi ke database di `DATABASES`
 - Mengatur berkas-berkas static (CSS, JavaScript, gambar, dsb.) di `STATIC_ROOT` dan `STATIC_URL`
 - Mengatur koneksi data cache di `CACHE`
 - Mengatur *cookies*
 - Mengatur pelaporan error dan *logging*

## 4: Bagaimana cara kerja migrasi database di Django?

Migrasi model merupakan cara Django menghubungkan perubahan yang kita lakukan pada model dengan skema data yang ada di *database* kita. Maksudnya, ketika kita mengubah model kita sedemikian rupa sehingga cara kerja *database* kita perlu berubah, migrasi bertugas untuk ikut memperbarui *database* kita untuk menerima perubahan tersebut.

Mengutip Django Software Foundation (2025), cara kerja migrasi database adalah seperti berikut:
 - Kita melakukan *command* `python manage.py makemigrations tasaki_shop` di terminal.
 - Django akan mengecek model kita, membandingkannya dengan model yang sudah disimpan sebelumnya, dan melaporkan perubahan-perubahan yang terlihat antara kedua model tersebut di terminal.
 - Django akan menciptakan *migration file* yang berisi perubahan-perubahan tersebut. Berkas ini akan disimpan di folder `migrations` di `main`.
 - Kita menginput `python manage.py migrate` untuk *commit* migrasi tersebut.
 - Jika kita *push* migrasi sekaligus dengan perubahan model, kita akan mendapatkan proyek Django dengan model yang diubah, beserta skema *database* yang telah disesuaikan untuk perubahan tersebut.

## 5: Dari semua framework yang ada, mengapa Django dijadikan permulaan pembelajaran *software development*?

Bagi saya, alasan utama Django dipilih adalah karena berdasarkan bahasa Python. Sebagai bahasa yang *interpreted* dan memiliki sintaks yang sederhana, Python cocok untuk memperkenalkan logika pemrograman kepada pemula. Selain itu, mahasiswa Fasilkom UI sudah memiliki pengalaman bekerja dengan Python melalui mata kuliah DDP 1 dan lainnya. Dasar Python ini memberikan Django keuntungan yang besar di *use case* ini dibandingkan framework lain, seperti Spring yang berbasis Java atau Laravel yang berbasis PHP.

## 6. Apakah ada feedback untuk kakak asdos dari sesi lab sebelumnya?

Kakak asdos standby di server discord PBP dan sangat cepat dalam menanggapi pertanyaan mahasiswa.

### Referensi:
Django Software Foundation. (2025). Dokumentasi Django versi 5.2. Diakses dari https://docs.djangoproject.com

