import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

# Load Data
day_df = pd.read_csv("https://raw.githubusercontent.com/hannatashyaa/bike/refs/heads/main/day.csv")

# Convert date column
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Mapping musim berdasarkan kode
season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
day_df['season_name'] = day_df['season'].map(season_map)

# Sidebar Filters
st.sidebar.header("Filter Data")

# Date range filter
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()
start_date, end_date = st.sidebar.date_input("Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])

# Filter berdasarkan rentang tanggal
filtered_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & (day_df["dteday"] <= pd.to_datetime(end_date))]

# Deteksi musim berdasarkan rentang tanggal yang dipilih
if not filtered_df.empty:
    detected_seasons = filtered_df['season_name'].unique()
    detected_seasons_str = ", ".join(sorted(detected_seasons))  # Urutkan musim agar lebih rapi
else:
    detected_seasons_str = "Tidak ada data dalam rentang tanggal yang dipilih"

# Dashboard Title
st.title("Bike Sharing Analysis Dashboard")

# **Daily Orders**
st.subheader("Daily Orders")

col1, col2 = st.columns(2)

with col1:
    total_orders = filtered_df['cnt'].sum()
    st.metric("Total Orders", value=total_orders)

with col2:
    total_revenue = format_currency(total_orders * 5, "USD", locale='en_US')  # Anggap harga sewa per unit = $5
    st.metric("Total Revenue", value=total_revenue)

# Plot Daily Orders
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(
    filtered_df["dteday"],
    filtered_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.set_xlabel("Tanggal", fontsize=12)
ax.set_ylabel("Jumlah Penyewaan", fontsize=12)
ax.set_title("Tren Daily Orders", fontsize=14)
ax.grid(True)
st.pyplot(fig)

# **Tampilkan musim yang terdeteksi**
st.subheader(f"Musim yang terdeteksi: {detected_seasons_str}")

# **Total Penyewaan Berdasarkan Musim**
st.subheader("Total Penyewaan Sepeda Berdasarkan Musim")
if not filtered_df.empty:
    season_rentals = filtered_df.groupby("season_name")['cnt'].sum()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=season_rentals.index, y=season_rentals.values, palette="Blues")
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Penyewaan")
    plt.title("Total Penyewaan Sepeda per Musim")
    st.pyplot(plt)
else:
    st.write("Tidak ada data yang tersedia untuk ditampilkan.")

# **Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari**
st.subheader("Pola Penyewaan Sepeda Berdasarkan Jam dalam Sehari")
hour_df = pd.read_csv("https://raw.githubusercontent.com/hannatashyaa/bike/refs/heads/main/hour.csv")
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
plt.figure(figsize=(10, 5))
hourly_rentals = hour_df.groupby("hr")['cnt'].sum()
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker="o", linestyle="-", color="blue")
plt.xlabel("Jam")
plt.ylabel("Jumlah Penyewaan")
plt.title("Pola Penyewaan Sepeda per Jam")
st.pyplot(plt)

# **Display Filtered Data**
st.subheader(f"Data Penyewaan Sepeda untuk Musim: {detected_seasons_str}")
if not filtered_df.empty:
    st.dataframe(filtered_df[['dteday', 'cnt', 'registered', 'casual']].head())
else:
    st.write("Tidak ada data yang tersedia dalam rentang tanggal yang dipilih.")

# **Menyiapkan Data RFM**
st.subheader("Best Customer Based on RFM Parameters")

# Simulasi data RFM dari dataframe day_df
rfm_df = filtered_df[['dteday', 'cnt']].copy()

# Recency: Selisih hari dari transaksi terakhir
rfm_df['Recency'] = (rfm_df['dteday'].max() - rfm_df['dteday']).dt.days

# Frequency: Jumlah transaksi yang dilakukan
rfm_df['Frequency'] = rfm_df.groupby(rfm_df['dteday'].dt.date)['cnt'].transform('count')

# Monetary: Total jumlah transaksi
rfm_df['Monetary'] = rfm_df.groupby(rfm_df['dteday'].dt.date)['cnt'].transform('sum')

# Menentukan segmen pelanggan secara sederhana
rfm_df['Segment'] = pd.qcut(rfm_df['Monetary'], q=4, labels=['Low', 'Mid', 'High', 'Very High'])

# **Menampilkan RFM Metrics**
col1, col2, col3 = st.columns(3)

with col1:
    avg_recency = round(rfm_df.Recency.mean(), 1)
    st.metric("Average Recency (days)", value=avg_recency)

with col2:
    avg_frequency = round(rfm_df.Frequency.mean(), 2)
    st.metric("Average Frequency", value=avg_frequency)

with col3:
    avg_monetary = format_currency(rfm_df.Monetary.mean(), "AUD", locale='es_CO')
    st.metric("Average Monetary", value=avg_monetary)

# **Visualisasi RFM Segments**
fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(y=rfm_df['Segment'], order=rfm_df['Segment'].value_counts().index, palette='viridis')
plt.title('Distribusi Segmen Pelanggan')
plt.xlabel('Jumlah')
plt.ylabel('Segmen')
st.pyplot(fig)

# **Menampilkan Sample Data RFM**
st.subheader("Sample RFM Data")
st.dataframe(rfm_df[['dteday', 'Recency', 'Frequency', 'Monetary', 'Segment']].head())

st.caption('Copyright (c) Bike Sharing Analysis 2025')
