# PDF Arama Aracı

Bu araç, PDF dosyalarında belirli bir kelime veya ifade içeren sayfaları tespit edip, bu sayfalardan oluşan yeni bir PDF dosyası oluşturur.

## Özellikler

- PDF içerisinde anahtar kelime/ifade araması yapma
- Büyük/küçük harf duyarlılığı seçeneği
- Eşleşen sayfalardan yeni bir PDF dosyası oluşturma
- İşlem detaylarını terminal ekranında gösterme

## Gereksinimler

- Python 3.x
- PyPDF2 kütüphanesi

## Kurulum

1. Gerekli kütüphaneyi yükleyin:

```bash
pip install PyPDF2
```

2. Programı indirin ve kullanıma başlayın.

## Kullanım

1. Script içinde `input_pdf_path` değişkenini kendi PDF dosyanızın adıyla değiştirin:

```python
input_pdf_path = "DOSYA_ADI_GIRIN"  # "DOSYA ADI GIRIN" yazan kısmı değiştirin
```

2. Scripti çalıştırın:

```bash
python main.py
```

3. Aramak istediğiniz kelime/ifadeyi girin
4. Büyük/küçük harf duyarlılığını belirtin (E/H)
5. Program eşleşen sayfaları içeren "cikti.pdf" dosyasını oluşturacaktır

## Örnek Kullanım

```
PDF içinde aramak istediğiniz kelimeyi girin:
> fatura
Büyük/küçük harf duyarlı arama yapmak istiyor musunuz? (E/H)
> h
'fatura' ifadesi içeren sayfalar aranıyor: ornek.pdf
Toplam 25 sayfa taranıyor...
Sayfa 3: Eşleşme bulundu
Sayfa 8: Eşleşme bulundu
Sayfa 17: Eşleşme bulundu

İşlem tamamlandı:
- 3 sayfa 'fatura' ifadesini içeriyordu.
- Çıktı dosyası: cikti.pdf
```

## Notlar

- Program, belirtilen kelimeyi içeren tüm sayfaları yeni PDF'e ekler
- Çıktı dosyası her zaman "cikti.pdf" adıyla kaydedilir
- PDF dosyası script ile aynı dizinde olmalıdır
