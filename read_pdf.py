import pypdf, logging, os, glob

def extract_text_from_pdf(filename):
    r = pypdf.PdfReader(filename)
    logging.info(f'Reading {len(r.pages)} pages from {filename}')
    text = "";
    for page in r.pages:
        text += page.extract_text()
    return text

def print_all_filenames_recursively(path):
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_dir():
            logging.info(entry.name)
            print_all_filenames_recursively(entry)
        if entry.is_file():
            logging.info(entry.name)

def find_all_files_by_extension(path, extension):
    return glob.glob(path  + "/**/*" + extension, recursive=True);

def save_text_in_file(text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def get_only_letters_space_from_string(text):
    return "".join(char for char in text if char.isalpha() or char.isspace())

def extract_all_texts_from_all_files(path, extension):
    fileList = find_all_files_by_extension(path, extension)
    logging.info(str(len(fileList)) + " files found.")

    allPDFsTest = "";
    for filename in fileList:
            allPDFsTest += filename + "\n"

    for filename in fileList:
        allPDFsTest += "\n" + filename + " :\n"
        allPDFsTest += extract_text_from_pdf(filename) + "\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
    save_text_in_file(allPDFsTest, get_only_letters_space_from_string(path)+"-output.txt")

logging.basicConfig(level=logging.INFO)

extract_all_texts_from_all_files(r"C:\mypath", ".pdf")
