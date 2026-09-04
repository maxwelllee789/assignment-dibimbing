import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ==========================================
# CONFIG & HEADER
# ==========================================
st.set_page_config(
    page_title="My Portfolio with Streamlit",
    page_icon="🏡",
    layout="wide"
)

# Sidebar Navigasi
st.sidebar.title("📌 Menu Pilihan")
menu = st.sidebar.radio(
    "Poin yang tersedia:",
    ["Tentang Saya & Proyek", "Visualisasi Data & Model", "Prediksi Harga Rumah"]
)

# ==========================================
# HALAMAN 1: TENTANG SAYA & PROYEK
# ==========================================
if menu == "Tentang Saya & Proyek":
    st.title("My Portfolio with Streamlit")
    st.markdown(
        "Tujuan dari project ini adalah pengembangan proyek untuk Assignment Day 50 - terkait dengan pembuatan portofolio"
        " dengan Streamlit."
    )
    st.divider()

    # Bagian 1: Tentang Saya
    st.header("👤 Bagian 1: Tentang Saya")

    col_bio, col_skills = st.columns([2, 1])

    with col_bio:
        st.markdown("### **Maxwell Asman**")
        st.markdown("#### *IT Advisory Specialist and Data Analytics*")
        
        # --- Latar Belakang Pendidikan (dengan HTML/CSS agar Rapat) ---
        st.markdown("<br><b>Latar Belakang Pendidikan:</b>", unsafe_allow_html=True)
        st.markdown(
            """
            <ul style="margin-left: 0px; padding-left: 18px; list-style-position: inside;">
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    <b>S1 Teknik Sipil</b> - Universitas Atma Jaya Yogyakarta (Jan 2018 - Jan 2022)
                    <br><i>IPK: 3.80 / 4.00 (Cum laude)</i>
                </li>
            </ul>
            """,
            unsafe_allow_html=True
        )

        # --- Pengalaman Kerja (dengan HTML/CSS agar Rapat) ---
        st.markdown("<br><b>Pengalaman Kerja:</b>", unsafe_allow_html=True)
        st.markdown(
            """
            <ul style="margin-left: 0px; padding-left: 18px; list-style-position: inside;">
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    🏦 <b>CIMB Niaga</b> | <i>IT Advisory Specialist and Data Analytics</i> (Apr 2024 - Present)
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    Mengevaluasi <i>risk assessment</i> & <i>audit reporting</i> sistem perbankan internal serta mendukung kepatuhan regulasi.
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    Mengembangkan <i>Bank-wide AI Governance Framework</i> dan inisiatif <i>Regional AI</i> untuk otomatisasi & <i>data-driven monitoring</i>.
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    Melakukan analisis data untuk deteksi pola anomali, risiko operasional, serta sistem <i>early warning alert</i>.
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    💳 <b>BCA Digital</b> | <i>Business Alignment</i> (Apr 2022 - Apr 2024)
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    Mengembangkan <i>Business Process Improvement (Kaizen)</i> yang meningkatkan efisiensi pembukaan rekening hingga 55%.
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    Mengolah data & visualisasi untuk menghasilkan <i>business insights</i> serta rencana aksi strategis.
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    Mengordinasikan perizinan valas ke OJK & BI serta menyusun SOP operasional perbankan.
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    🏗️ <b>Adhi Karya Tbk</b> | <i>Supervisor Intern</i> (Jan 2021 - Mar 2021)
                </li>
                <li style="margin-bottom: 5px; padding-left: 0px; text-indent: 0px;">
                    Supervisi operasional harian proyek konstruksi dan penyusunan laporan progres.
                </li>
            </ul>
            """,
            unsafe_allow_html=True
        )

    with col_skills:
        # Bagian Keahlian tetap sama seperti sebelumnya
        st.markdown("### **Keahlian**")
        st.markdown("""
        **Data & Analytics:**
        - SQL
        - Power BI
        - Tableau
        - Data Analytics & Monitoring

        **AI & IT Governance:**
        - AI Governance
        - IT Governance
        - Risk Assessment
        - Audit Review
        - Regulatory Compliance

        **Business Process:**
        - Business Process Improvement
        - Stakeholder Management
        """)

    st.divider()

    # Bagian 2: Proyek Saya
    st.header("📂 Bagian 2: Proyek Saya")
    st.write("Berikut adalah beberapa proyek machine learning yang pernah saya kembangkan:")

    proj1, proj2, proj3 = st.columns(3)

    with proj1:
        st.subheader("1. House Prices MLOps")
        st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500", caption="House Price Prediction")
        st.write("Implementasi pipeline regresi *end-to-end* menggunakan dataset Kaggle House Prices dengan MLOps best practice.")
        if st.button("Detail Proyek House Prices"):
            st.info("Proyek ini menggunakan XGBoost dan Random Forest dengan *Hyperparameter Tuning*.")

    with proj2:
        st.subheader("2. Coming Soon")
        st.image("https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=500", caption="Hanya Testing 1")
        st.write("Section ini belum tesedia untuk diinformasikan. *Coming Soon* untuk portofolio berikutnya.")
        if st.button("Coming Soon1"):
            st.info("Coming Soon")

    with proj3:
            st.subheader("3. Coming Soon")
            st.image("https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=500", caption="Hanya Testing 2")
            st.write("Section ini belum tesedia untuk diinformasikan. *Coming Soon* untuk portofolio berikutnya.")
            if st.button("Coming Soon2"):
                st.info("Coming Soon")


# ==========================================
# HALAMAN 2: VISUALISASI DATA & MODEL
# ==========================================
elif menu == "Visualisasi Data & Model":
    st.title("📊 Visualisasi Data dan Performa Model")
    st.write("Analisis eksplorasi data (EDA) dan evaluasi performa model Machine Learning.")

    # Generator Data Dummy untuk Visualisasi
    np.random.seed(42)
    sample_size = 200
    df_sample = pd.DataFrame({
        'GrLivArea': np.random.normal(1500, 500, sample_size),
        'OverallQual': np.random.randint(1, 10, sample_size),
        'GarageCars': np.random.randint(0, 4, sample_size),
        'TotalBsmtSF': np.random.normal(1000, 300, sample_size),
        'SalePrice': np.random.normal(180000, 50000, sample_size)
    })

    tab_data, tab_model = st.tabs(["📈 Analisis Dataset (EDA)", "🎯 Performa Model ML"])

    with tab_data:
        st.subheader("Distribusi & Korelasi Fitur Dataset")
        
        col_fig1, col_fig2 = st.columns(2)
        
        with col_fig1:
            st.write("**Distribusi Harga Rumah (SalePrice)**")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.histplot(df_sample['SalePrice'], kde=True, ax=ax, color='skyblue')
            ax.set_title("Distribusi Target (SalePrice)")
            st.pyplot(fig)

        with col_fig2:
            st.write("**Matriks Korelasi Antar Fitur**")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.heatmap(df_sample.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            ax.set_title("Correlation Heatmap")
            st.pyplot(fig)

    with tab_model:
        st.subheader("Evaluasi Performa Model Interaktif")
        
        # Opsi Interaktif Pilihan Model
        selected_model = st.selectbox(
            "Pilih Model untuk Divisualisasikan:",
            ["XGBoost Regressor", "Random Forest Regressor", "Linear Regression"]
        )

        # Mock Metrik Berdasarkan Model
        metrics = {
            "XGBoost Regressor": {"RMSE": 23400.5, "MAE": 15200.1, "R2": 0.89},
            "Random Forest Regressor": {"RMSE": 25100.8, "MAE": 16800.4, "R2": 0.86},
            "Linear Regression": {"RMSE": 32000.2, "MAE": 21000.0, "R2": 0.75}
        }

        m = metrics[selected_model]

        # Menampilkan Metrik
        col_m1, col_m2, col_m3 = st.columns(3)
        col_m1.metric("RMSE", f"${m['RMSE']:,.2f}")
        col_m2.metric("MAE", f"${m['MAE']:,.2f}")
        col_m3.metric("R² Score", f"{m['R2']:.2f}")

        st.divider()

        # Visualisasi Actual vs Predicted
        y_true = np.random.normal(180000, 50000, 50)
        noise = np.random.normal(0, m['RMSE'] * 0.5, 50)
        y_pred = y_true + noise

        fig_pred, ax_pred = plt.subplots(figsize=(8, 4))
        ax_pred.scatter(y_true, y_pred, alpha=0.7, color='green')
        ax_pred.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--', lw=2)
        ax_pred.set_xlabel("Actual SalePrice")
        ax_pred.set_ylabel("Predicted SalePrice")
        ax_pred.set_title(f"Actual vs Predicted - {selected_model}")
        st.pyplot(fig_pred)


# ==========================================
# HALAMAN 3: PREDIKSI HARGA RUMAH (INFERENCE)
# ==========================================
elif menu == "Prediksi Harga Rumah":
    st.title("🏡 Bagian 3: Pipeline Prediksi Berbasis Model")
    st.write("Unggah file data tes (format `.csv`) untuk menjalankan pipeline prediksi harga rumah secara otomatis.")

    uploaded_file = st.file_uploader("Upload File Dataset (CSV)", type=["csv"])

    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        st.write("### Preview Data Input:")
        st.dataframe(input_df.head())

        # Button Trigger Pipeline
        if st.button("🚀 Jalankan Pipeline Prediksi"):
            with st.spinner("Menjalankan preprocessing data dan inferensi model..."):
                # Simulasi Proses Prediksi Pipeline
                # Catatan: Integrasikan joblib.load('model.pkl') di bagian ini untuk implementasi riil.
                
                # Menambahkan kolom prediksi dummy
                df_result = input_df.copy()
                df_result['Predicted_SalePrice'] = np.random.normal(180000, 40000, len(input_df))

            st.success("Prediksi Berhasil Diselesaikan!")
            st.write("### Hasil Prediksi:")
            st.dataframe(df_result[['Predicted_SalePrice'] + [col for col in input_df.columns if col != 'Predicted_SalePrice']].head(10))

            # Download Button
            csv_data = df_result.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Hasil Prediksi (CSV)",
                data=csv_data,
                file_name="house_price_predictions.csv",
                mime="text/csv"
            )
    else:
        st.info("Silakan unggah file CSV berisi fitur rumah untuk memulai prediksi.")