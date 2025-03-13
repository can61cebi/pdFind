import os
from PyPDF2 import PdfReader, PdfWriter


def extract_pages_with_keyword(keyword, case_sensitive=False):
    """
    PDF içerisinde belirtilen kelimeyi içeren sayfaları ayırarak yeni bir PDF oluşturur.

    Args:
        keyword (str): Aranacak kelime veya ifade
        case_sensitive (bool): Büyük/küçük harf duyarlılığı (Varsayılan: False)

    Returns:
        tuple: (başarılı_mı (bool), bulunan_sayfa_sayısı (int))
    """
    # Sabit dosya isimleri
    input_pdf_path = "DOSYA ADI GIRIN"  # PDF dosyası script ile aynı klasörde
    output_pdf_path = "cikti.pdf"  # Çıktı sabit olarak "cikti.pdf"

    print(f"'{keyword}' ifadesi içeren sayfalar aranıyor: {input_pdf_path}")

    if not os.path.exists(input_pdf_path):
        print(f"Hata: Dosya bulunamadı: {input_pdf_path}")
        return False, 0

    try:
        # PDF'i okuyalım
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        # Toplam sayfa sayısı
        total_pages = len(reader.pages)
        print(f"Toplam {total_pages} sayfa taranıyor...")

        # Eşleşen sayfalar için liste
        matched_pages = []

        # Her sayfayı kontrol edelim
        for page_num, page in enumerate(reader.pages):
            # Sayfadaki metni çıkaralım
            text = page.extract_text()

            # Büyük/küçük harf duyarlılığı kontrolü
            if not case_sensitive:
                search_text = text.lower()
                search_keyword = keyword.lower()
            else:
                search_text = text
                search_keyword = keyword

            # Kelime kontrolü
            if search_keyword in search_text:
                matched_pages.append(page_num)
                writer.add_page(page)
                print(f"Sayfa {page_num + 1}: Eşleşme bulundu")

        # Eşleşme bulunamadıysa
        if not matched_pages:
            print(f"'{keyword}' ifadesi hiçbir sayfada bulunamadı.")
            return True, 0

        # Yeni PDF'i kaydedelim
        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)

        print(f"\nİşlem tamamlandı:")
        print(f"- {len(matched_pages)} sayfa '{keyword}' ifadesini içeriyordu.")
        print(f"- Çıktı dosyası: {output_pdf_path}")

        return True, len(matched_pages)

    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        return False, 0


def main():
    # Kullanıcıdan aranacak kelimeyi alıyoruz
    print("PDF içinde aramak istediğiniz kelimeyi girin:")
    keyword = input("> ")

    # Büyük/küçük harf duyarlı arama yapmak istiyor mu?
    print("Büyük/küçük harf duyarlı arama yapmak istiyor musunuz? (E/H)")
    case_sensitive = input("> ").strip().lower() == "e"

    # Aramayı başlat
    extract_pages_with_keyword(keyword, case_sensitive)


if __name__ == "__main__":
    main()