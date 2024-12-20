import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Memuat dataset yang telah dibersihkan dan digabungkan sebelumnya
df_combined = pd.read_csv('dashboard/main_data.csv') 

# Judul Aplikasi Streamlit
st.title('Dashboard Analisis Peminjaman Sepeda')

# Deskripsi Aplikasi
st.write("""
    **Selamat datang di aplikasi analisis data peminjaman sepeda.**
    \n
    *Noted: Pilih visualisasi untuk memulai eksplorasi.*
""")

# Menambahkan Pilihan Menu untuk Visualisasi
option = st.sidebar.selectbox(
    'Pilih Visualisasi:',
    ('Pengaruh Cuaca terhadap Peminjaman Sepeda', 
     'Pola Peminjaman Sepeda berdasarkan Jam', 
     'Pola Peminjaman Sepeda berdasarkan Hari dalam Seminggu')
)

# Visualisasi Pengaruh Cuaca terhadap Peminjaman Sepeda
if option == 'Pengaruh Cuaca terhadap Peminjaman Sepeda':
    st.subheader('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')

    # Visualisasi Boxplot untuk Cuaca
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weathersit_hour', y='cnt_day', data=df_combined)
    plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.xticks([0, 1, 2, 3], ['Clear', 'Misty', 'Light Snow', 'Heavy Snow'])
    st.pyplot(plt)

# Visualisasi Pola Peminjaman Sepeda berdasarkan Jam
elif option == 'Pola Peminjaman Sepeda berdasarkan Jam':
    st.subheader('Pola Peminjaman Sepeda Berdasarkan Jam')

    # Visualisasi Lineplot untuk Jam
    hourly_usage = df_combined.groupby('hr')['cnt_hour'].mean()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=hourly_usage.index, y=hourly_usage.values)
    plt.title('Pola Peminjaman Sepeda Berdasarkan Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    st.pyplot(plt)

# Visualisasi Pola Peminjaman Sepeda berdasarkan Hari dalam Seminggu
elif option == 'Pola Peminjaman Sepeda berdasarkan Hari dalam Seminggu':
    st.subheader('Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')

    # Visualisasi Barplot untuk Hari dalam Seminggu
    weekday_usage = df_combined.groupby('weekday_day')['cnt_day'].mean()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=weekday_usage.index, y=weekday_usage.values)
    plt.title('Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    st.pyplot(plt)
