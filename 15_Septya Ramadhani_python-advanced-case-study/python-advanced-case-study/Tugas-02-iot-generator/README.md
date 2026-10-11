# Streaming Data Sensor IoT

## Deskripsi
Program ini menyimulasikan pembacaan suhu sensor. Data dibaca satu per satu, lalu dikelompokkan menjadi dingin, normal, atau panas.

## Konsep Python yang Digunakan
- **Generator Function:** memakai `yield` untuk menghasilkan suhu bertahap.
- **Iterator:** mengambil data satu per satu menggunakan `next()`.
- **Efisiensi Memori:** data diproses bertahap tanpa membuat list baru untuk semua hasil.

## Kategori Suhu
- Dingin: di bawah 20°C.
- Normal: 20°C sampai 30°C.
- Panas: di atas 30°C.

## Cara Menjalankan
1. Buka folder `case-02-iot-generator` di VS Code.
2. Jalankan `python main.py` melalui terminal.
3. Hasil pembacaan suhu muncul di terminal.

Screenshot hasil program ada di `output.png`.
