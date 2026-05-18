import pypdf, logging

def read_pdf_pages(filePath):
    r = pypdf.PdfReader(filePath)
    logging.info(f'Reading {len(r.pages)} pages from {filePath}')
    text = "";
    for page in r.pages:
        text += page.extract_text()
    return text

logging.basicConfig(level=logging.INFO)
fileName = r"example.pdf";
print(read_pdf_pages(fileName))
