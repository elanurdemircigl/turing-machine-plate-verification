# Turing Makinesi ile Plaka Doğrulama

Bu proje, bir Turing Makinesi kullanarak belirli bir plaka formatının doğruluğunu kontrol eden bir Python simülasyonudur.

## 📌 Proje Hakkında
Bu proje, girdi olarak verilen bir plakayı karakter karakter inceler ve belirlenen sonlu durum makinesi kurallarına göre kabul veya red kararı verir.

### Kabul Edilen Format: `99AA999`
Makine şu kural dizisini takip eder:
1.  **q0-q1:** İlk iki karakter rakam olmalı.
2.  **q2-q3:** Sonraki iki karakter büyük harf olmalı.
3.  **q4-q6:** Son üç karakter rakam olmalı.
4.  **q7:** Kabul durumu.

## 🚀 Çalıştırma
Kodu yerel makinenizde çalıştırmak için:

```bash
python main.py
