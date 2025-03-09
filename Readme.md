# Proyek Analisis Data: Bike Sharing Dataset

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data peminjaman sepeda berdasarkan musim dan pola penggunaan dalam sehari. Selain itu, dilakukan analisis lanjutan menggunakan RFM Analysis untuk mengelompokkan pelanggan berdasarkan perilaku peminjaman mereka.

## Pertanyaan Bisnis
1. Bagaimana pengaruh musim terhadap jumlah peminjaman sepeda?
2. Bagaimana tren penggunaan sepeda berdasarkan waktu dalam sehari?

## Struktur Direktori
```
submission/
├── dashboard/
│   ├── dashboard.py          # Aplikasi Streamlit
│   └── requirements.txt      # Library untuk dashboard
├── data/
│   ├── day.csv               # Dataset harian
│   └── hour.csv              # Dataset per jam
├── notebook.ipynb            # Notebook analisis data
├── README.md                 # Dokumentasi proyek
├── requirements.txt          # Daftar library untuk proyek
└── url.txt                   # URL dashboard (jika tersedia)
```

## Instalasi dan Menjalankan Proyek
### **Menjalankan Analisis Data**  
1. Pastikan Anda memiliki Jupyter Notebook atau Google Colab.
2. Buka `notebook.ipynb` dan jalankan semua sel untuk melihat hasil analisis.

### **Menjalankan Dashboard (Streamlit)**  
1. Instal library yang diperlukan dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan dashboard dengan perintah:
   ```bash
   streamlit run dashboard/dashboard.py
   ```
3. Dashboard akan terbuka di browser web default Anda.

## Fitur Dashboard
Dashboard ini menyediakan beberapa fitur utama:
- **Filter Data** berdasarkan musim dan waktu.
- **Visualisasi interaktif** untuk memahami pola peminjaman sepeda.
- **Analisis RFM** untuk mengelompokkan pelanggan berdasarkan perilaku mereka.

## Kesimpulan Utama
1. **Musim memiliki dampak signifikan terhadap jumlah peminjaman sepeda**, dengan musim panas dan gugur mencatat jumlah peminjaman tertinggi.
2. **Peminjaman sepeda meningkat pada jam sibuk (pagi dan sore)**, terutama oleh pengguna terdaftar (registered).
3. **Cuaca juga mempengaruhi pola peminjaman**, dengan jumlah peminjaman menurun saat kondisi cuaca buruk.

## Rekomendasi Bisnis
1. **Strategi Marketing**:
   - Kampanye promosi pada musim dengan peminjaman rendah.
   - Paket berlangganan fleksibel untuk menarik lebih banyak pengguna casual.
2. **Operasional**:
   - Penyesuaian jumlah sepeda berdasarkan tren penggunaan harian.
   - Optimasi lokasi penyebaran sepeda berdasarkan pola peminjaman.
3. **Pengembangan Produk**:
   - Penyempurnaan layanan pemesanan dan rekomendasi berdasarkan pola penggunaan.

## Sumber Data
Dataset yang digunakan dalam proyek ini adalah Bike Sharing Dataset dari [sumber data](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset).

## Penulis
**Hanna Tashya Portuna**  
Email: mc185d5x0288@student.devacademy.id  
ID Dicoding: MC185D5X0288

---
© 2025 Bike Sharing Analysis Project  
Proyek ini dikembangkan sebagai bagian dari submission Dicoding "Belajar Analisis Data dengan Python".
