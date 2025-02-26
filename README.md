# SecurityTrails-Subdomain-Finder 🕵️♂️

Tool Python untuk menemukan subdomain secara lengkap menggunakan API SecurityTrails. Dilengkapi pagination, penyimpanan hasil ke file, dan antarmuka interaktif.

## Fitur Utama
- ✅ **Pencarian Subdomain Lengkap**  
  Menggunakan API SecurityTrails dengan pagination otomatis untuk mengambil semua subdomain (termasuk hasil ratusan/ribu).
- ✅ **Filter Subdomain Langsung**  
  Opsi `children_only` untuk mengambil hanya subdomain langsung (*tanpa nested subdomains*).
- ✅ **Penyimpanan Otomatis**  
  Hasil disimpan ke file `results_<domain>.txt` untuk analisis lebih lanjut.
- ✅ **Antarmuka User-Friendly**  
  Progress indicator, validasi API key, dan penanganan error yang jelas.
- ✅ **Rate-Limited Requests**  
  Menghindari API abuse dengan delay antar-request (0.3 detik/halaman).

## Persyaratan
- Python 3.6+
- Library `requests`
- API Key SecurityTrails ([Daftar Disini](https://securitytrails.com/))

## Instalasi
1. Clone repositori:
   ```bash
   git clone https://github.com/username/SecurityTrails-Subdomain-Finder.git
