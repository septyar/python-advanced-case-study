# Keamanan Login dan Audit Log

## Deskripsi
Program ini memeriksa format username dan password saat login. Program juga mencatat waktu, username, status login, dan alasan jika login ditolak.

## Konsep Python yang Digunakan
- **RegEx:** memeriksa format username dan password.
- **Class dan `@property`:** mengatur atribut username dan password.
- **Decorator dan Closure:** mencatat hasil percobaan login secara otomatis.

## Aturan Validasi
- Username minimal 5 karakter dan hanya menggunakan huruf serta angka.
- Password minimal 8 karakter dan harus memiliki setidaknya satu angka.

## Cara Menjalankan
1. Buka folder `case-03-login-security` di VS Code.
2. Jalankan `python main.py` melalui terminal.
3. Hasil beberapa percobaan login akan muncul di terminal.

Screenshot hasil program ada di `output.png`.

Catatan: program ini adalah simulasi validasi format untuk tugas, bukan sistem login produksi.
