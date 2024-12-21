import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

# Memuat dataset yang telah dibersihkan dan digabungkan sebelumnya
df_combined = pd.read_csv('dashboard/main_data.csv')

# Pastikan untuk menambahkan kolom 'weekday_day' jika belum ada
df_combined['weekday_day'] = pd.to_datetime(df_combined['dteday_day']).dt.weekday
df_combined['dteday_day'] = pd.to_datetime(df_combined['dteday_day'])

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

# Filtering Berdasarkan Tanggal
st.sidebar.subheader("Filter Berdasarkan Tanggal")
start_date = st.sidebar.date_input("Tanggal Mulai", df_combined['dteday_day'].min())
end_date = st.sidebar.date_input("Tanggal Akhir", df_combined['dteday_day'].max())

# Filter dataset berdasarkan tanggal yang dipilih
df_filtered = df_combined[(df_combined['dteday_day'] >= pd.to_datetime(start_date)) & (df_combined['dteday_day'] <= pd.to_datetime(end_date))]

# Filtering Berdasarkan Cuaca
st.sidebar.subheader("Filter Berdasarkan Cuaca")
weather_condition = st.sidebar.selectbox(
    'Pilih Kondisi Cuaca:',
    ['All', 'Clear', 'Misty', 'Light Snow', 'Heavy Snow']
)

# Filter dataset berdasarkan cuaca
if weather_condition != 'All':
    df_filtered = df_filtered[df_filtered['weathersit_hour'] == {'Clear': 1, 'Misty': 2, 'Light Snow': 3, 'Heavy Snow': 4}[weather_condition]]

# Visualisasi Pengaruh Cuaca terhadap Peminjaman Sepeda
if option == 'Pengaruh Cuaca terhadap Peminjaman Sepeda':
    st.subheader('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')

    # Mapping nilai numerik ke label cuaca
    weather_mapping = {1: 'Clear', 2: 'Misty', 3: 'Light Snow', 4: 'Heavy Snow'}
    df_filtered['weathersit_hour_label'] = df_filtered['weathersit_hour'].map(weather_mapping)

    # Visualisasi Boxplot untuk Cuaca
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    sns.boxplot(x='weathersit_hour_label', y='cnt_day', data=df_filtered, order=['Clear', 'Misty', 'Light Snow', 'Heavy Snow'])
    plt.title('Pengaruh Cuaca terhadap Jumlah Peminjaman Sepeda')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman Sepeda')
    plt.tight_layout()
    st.pyplot(plt)

# Visualisasi Pola Peminjaman Sepeda berdasarkan Jam
elif option == 'Pola Peminjaman Sepeda berdasarkan Jam':
    st.subheader('Pola Peminjaman Sepeda Berdasarkan Jam')

    # Visualisasi Lineplot untuk Jam
    hourly_usage = df_filtered.groupby('hr')['cnt_hour'].mean()
    plt.figure(figsize=(12, 6))
    sns.set(style="whitegrid")
    sns.lineplot(x=hourly_usage.index, y=hourly_usage.values)
    plt.title('Pola Peminjaman Sepeda Berdasarkan Jam')
    plt.xlabel('Jam')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.tight_layout()
    st.pyplot(plt)

# Visualisasi Pola Peminjaman Sepeda berdasarkan Hari dalam Seminggu
elif option == 'Pola Peminjaman Sepeda berdasarkan Hari dalam Seminggu':
    st.subheader('Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')

    # Visualisasi Barplot untuk Hari dalam Seminggu
    weekday_usage = df_filtered.groupby('weekday_day')['cnt_day'].mean()
    plt.figure(figsize=(12, 6))
    sns.set(style="whitegrid")
    sns.barplot(x=weekday_usage.index, y=weekday_usage.values)
    plt.title('Pola Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    plt.tight_layout()
    st.pyplot(plt)
