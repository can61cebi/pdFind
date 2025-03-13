# PDF Search Tool

A tool that extracts pages containing specific keywords from PDF files and creates a new PDF with those pages. The program interface is in Turkish.

## Features

- Search for keywords/phrases within PDF documents
- Option for case-sensitive searching
- Generate a new PDF file containing only matching pages
- Display process details in terminal

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

1. Install the required library:

```bash
pip install PyPDF2
```

2. Download the program and start using it.

## Usage

1. Replace the `input_pdf_path` variable in the script with your PDF filename:

```python
input_pdf_path = "DOSYA_ADI_GIRIN"  # Replace the "DOSYA ADI GIRIN" part with your .pdf file
```

2. Run the script:

```bash
python pdf_search.py
```

3. The program will run in Turkish:
   - Enter the keyword when prompted for "PDF içinde aramak istediğiniz kelimeyi girin:"
   - Choose case sensitivity by answering "E" (yes) or "H" (no) when asked "Büyük/küçük harf duyarlı arama yapmak istiyor musunuz? (E/H)"
   - The program will create "cikti.pdf" containing the matching pages

## Example Output (in Turkish)

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

## Notes

- The program adds all pages containing the specified keyword to the new PDF
- The output file is always saved as "cikti.pdf"
- The PDF file should be in the same directory as the script
