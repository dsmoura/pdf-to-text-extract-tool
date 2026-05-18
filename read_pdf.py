import pypdf, logging, os, glob

def read_pdf_pages(filename):
    r = pypdf.PdfReader(filename)
    logging.info(f'Reading {len(r.pages)} pages from {filename}')
    text = "";
    for page in r.pages:
        text += page.extract_text()
    return text

def print_all_filenames_with_os(path):
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_dir():
            logging.info(entry.name)
            print_all_filenames_with_os(entry)
        if entry.is_file():
            logging.info(entry.name)

def print_all_filenames_with_glob(path):
    filesFound = 0;
    for name in glob.glob(path, recursive=True):
        print(name)
        filesFound += 1
    print(str(filesFound) + " files found.")

logging.basicConfig(level=logging.INFO)
fileName = r"example.pdf";
#print(read_pdf_pages(fileName))
