# 🏡 House Prices Prediction & Streamlit Portfolio

Aplikasi web interaktif yang dikembangkan menggunakan **Streamlit** untuk menampilkan portofolio profesional *Data Science*, visualisasi data/model, serta pipeline inferensi machine learning secara *end-to-end* untuk prediksi harga rumah (menggunakan dataset Kaggle *House Prices - Advanced Regression Techniques*).

---

## 📌 Deskripsi Proyek

Assignment ini berfokus pada implementasi praktik MLOps siap produksi. Aplikasi ini mencakup:
1. **Portofolio Interaktif:** Branding diri, profil profesional, latar belakang, serta daftar proyek *Machine Learning* yang pernah dikerjakan.
2. **Visualisasi Data & Model:** Analisis eksplorasi data (EDA) interaktif dan evaluasi performa model machine learning (RMSE, MAE, R² Score, serta grafik *Actual vs Predicted*).
3. **Pipeline Inferensi (Prediksi):** Fitur unggah file dataset tes (`.csv`), pemicu pipeline prediksi otomatis, dan opsi pengunduhan hasil prediksi.

---

## ✨ Fitur Utama

- **Navigasi Halaman:** Berpindah antar modul aplikasi dengan mudah melalui *sidebar*.
- **Opsi Interaktif:** Pilihan model machine learning secara dinamis untuk melihat metrik dan grafik performa.
- **Prediksi Otomatis:** Memuat model terpilih (`.pkl`) untuk memprediksi file CSV input secara langsung.
- **Ekspor Hasil:** Mengunduh hasil prediksi dalam format `.csv`.

---

## 🛠️ Teknologi & Tools

- **Bahasa Pemrograman:** Python
- **Framework Web:** Streamlit
- **Data Manipulation & Visualisasi:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn, Joblib
- **Version Control:** Git & GitHub

---

## 📁 Struktur Direktori

```text
.
├── app.py                   # Script utama aplikasi Streamlit
├── model_house_price.pkl    # File model machine learning yang sudah dilatih
├── requirements.txt         # Daftar pustaka/library Python yang dibutuhkan
├── .gitignore               # File penentu daftar berkas yang diabaikan Git
└── README.md                # Dokumentasi proyek
