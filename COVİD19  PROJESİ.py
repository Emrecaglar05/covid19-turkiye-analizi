import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("C:/Users/90505/Desktop/GİT-GİTHUB PROJE DOSYALARI/PROJE1/Covid19-Turkey-Turkce.csv")
print(df.columns)

def veri(df):
    print(df.shape)
    print(df.head(10))
    df.info()
    print(df.describe())
    print(df.isnull().sum())

def eksik_veri_analizi(df):
    df["Tarih"] = pd.to_datetime(df["Tarih"], format="%m/%d/%Y")

    # '=' ile başlayan satırları kaldırma işlemi yaptık
    df = df[~df["Toplam Yoğun Bakım Sayısı"].astype(str).str.startswith("=")]
    df["Toplam Yoğun Bakım Sayısı"] = pd.to_numeric(df["Toplam Yoğun Bakım Sayısı"], errors="coerce")

    sayisal_sutunlar = df.select_dtypes(include=['int64', 'float64']).columns
    for sutun in sayisal_sutunlar:
        df[sutun] = df[sutun].fillna(df[sutun].median())

    kategorik_sutunlar = df.select_dtypes(include=['object']).columns
    for sutun in kategorik_sutunlar:
        if sutun != 'Tarih':
            df[sutun] = df[sutun].fillna(df[sutun].mode()[0])

    if 'Tarih' in df.columns and df['Tarih'].isnull().any():
        df['Tarih'] = pd.to_datetime(df['Tarih'])
        df['Tarih'] = df['Tarih'].interpolate(method='time')

    return df


def vaka_gorseli(df):
    plt.figure(figsize=(15, 6))
    plt.plot(df["Tarih"], df["Günlük Vaka Sayısı"], label="Günlük Vakalar", color="brown")
    plt.title("Türkiye COVID-19 Günlük Vaka Sayıları")
    plt.xlabel("Tarih")
    plt.ylabel("Vaka Sayısı")
    plt.legend()
    plt.grid()

def olum_gorseli(df):
    plt.figure(figsize=(15, 6))
    plt.plot(df["Tarih"], df["Toplam Vaka Sayısı"], label="Toplam Vakalar", color="green")
    plt.plot(df["Tarih"], df["Toplam Vefat Sayısı"], label="Toplam Ölümler", color="red")
    plt.title('Türkiye COVID-19 Toplam Vaka ve Ölüm Sayıları')
    plt.xlabel('Tarih')
    plt.ylabel('Sayı')
    plt.legend()
    plt.grid()

def yogunbakim_gorseli(df):
    plt.figure(figsize=(15, 6))
    plt.plot(df['Tarih'], df['Toplam Yoğun Bakım Sayısı'], label='Yoğun Bakım', color='orange')
    plt.plot(df['Tarih'], df['Entübe Vaka Sayısı'], label='Entübe Hastalar', color='purple')
    plt.title('Yoğun Bakım ve Entübe Hasta Sayıları')
    plt.xlabel('Tarih')
    plt.ylabel('Sayı')
    plt.legend()
    plt.grid()

def pozitiflik_orani_gorseli(df):
    plt.figure(figsize=(12, 6))
    df['Pozitiflik_Orani'] = (df['Günlük Vaka Sayısı'] / df['Günlük Test Sayısı']) * 100
    plt.plot(df['Tarih'], df['Pozitiflik_Orani'], color='purple', linewidth=2, label='Pozitiflik Oranı (%)')
    plt.axhline(y=5, color='red', linestyle=':', linewidth=2, label='DSÖ Güvenli Eşik (≤%5)')
    plt.title('Türkiye COVID-19 Test Pozitiflik Oranı (2020)', fontsize=14, pad=20)
    plt.xlabel('Tarih', fontsize=12)
    plt.ylabel('Oran (%)', fontsize=12)
    plt.legend(loc='upper right', fontsize=10)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()

def korelasyon_gorseli(df):
    korelasyon = df.corr()
    plt.figure(figsize=(15, 10))
    sns.heatmap(korelasyon, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Değişkenler Arası Korelasyon Matrisi')
    return korelasyon

def hareketli_ortalama_gorseli(df):
    df['7_Gunluk_Hareketli_Ortalama'] = df['Günlük Vaka Sayısı'].rolling(window=7).mean()
    plt.figure(figsize=(15, 6))
    plt.plot(df['Tarih'], df['Günlük Vaka Sayısı'], label='Günlük Vakalar', alpha=0.5)
    plt.plot(df['Tarih'], df['7_Gunluk_Hareketli_Ortalama'], label='7 Günlük Hareketli Ortalama', color='red')
    plt.title('Günlük Vakalar ve 7 Günlük Hareketli Ortalama')
    plt.xlabel('Tarih')
    plt.ylabel('Vaka Sayısı')
    plt.legend()
    plt.grid()

def oran_gorselleri(df):
    df['Vaka_Test_Orani'] = df['Günlük Vaka Sayısı'] / df['Günlük Test Sayısı']
    df['Iyilesme_Orani'] = df['Toplam İyileşen Sayısı'] / df['Toplam Vaka Sayısı']
    df['Olum_Orani'] = df['Toplam Vefat Sayısı'] / df['Toplam Vaka Sayısı']
    df['Haftanin_Gunu'] = df['Tarih'].dt.day_name()
    df['Hafta_Sonu'] = df['Haftanin_Gunu'].isin(['Saturday', 'Sunday']).astype(int)

    plt.figure(figsize=(15, 6))
    plt.plot(df['Tarih'], df['Vaka_Test_Orani'], label='Vaka/Test Oranı', color='green')
    plt.title('Günlük Vaka/Test Oranı')
    plt.xlabel('Tarih')
    plt.ylabel('Oran')
    plt.legend()
    plt.grid()

def gorsellestirme(df):
    vaka_gorseli(df)
    olum_gorseli(df)
    yogunbakim_gorseli(df)
    pozitiflik_orani_gorseli(df)
    korelasyon = korelasyon_gorseli(df)
    hareketli_ortalama_gorseli(df)
    oran_gorselleri(df)
    plt.show()
    print("\nEn Yüksek Korelasyonlar:")
    print(korelasyon.unstack().sort_values(ascending=False).drop_duplicates().head(10))



df = eksik_veri_analizi(df)
veri(df)
gorsellestirme(df)
