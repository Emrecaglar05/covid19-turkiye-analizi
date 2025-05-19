# Türkiye COVID-19 Veri Analizi

Bu proje, [buradan indirilmiş olan COVID-19 Türkiye veri setini](https://www.kaggle.com) kullanarak temel veri analizi ve görselleştirmeler yapmaktadır.

## Kullanılan Kütüphaneler

* Pandas
* NumPy
* Matplotlib
* Seaborn

## Görselleştirmeler

Projede aşağıdaki temel görselleştirmeler oluşturulmuştur:

* **Günlük Vaka Sayısı:** Zaman içindeki günlük yeni vaka sayılarını gösteren çizgi grafik.
* **Toplam Vaka ve Ölüm Sayıları:** Zaman içindeki toplam vaka ve ölüm sayılarını karşılaştıran çizgi grafik.
* **Yoğun Bakım ve Entübe Hasta Sayıları:** Yoğun bakım ve entübe hasta sayılarının zaman içindeki değişimini gösteren çizgi grafik.
* **Pozitiflik Oranı:** Günlük test sayısına göre hesaplanan pozitiflik oranının zaman içindeki değişimi.
* **Korelasyon Matrisi:** Değişkenler arasındaki doğrusal ilişkileri gösteren ısı haritası.
* **Hareketli Ortalama:** Günlük vaka sayısının 7 günlük hareketli ortalaması.
* **Vaka/Test Oranı:** Günlük vaka sayısının günlük test sayısına oranının zaman içindeki değişimi.

## Nasıl Çalıştırılır

Bu proje için Python 3 ve yukarıda listelenen kütüphanelerin kurulu olması gerekmektedir. Kodu çalıştırmak için `python <COVİD19 PROJESİ>.py` komutunu kullanabilirsiniz. Veri dosyası (`Covid19-Turkey-Turkce.csv`) aynı dizinde olmalıdır.

## Gelecek Çalışmalar

* Daha fazla veri kaynağı entegrasyonu (örneğin, aşılama verileri).
* Zaman serisi tahmin modelleri uygulama.
* Etkileşimli görselleştirmeler oluşturma.
