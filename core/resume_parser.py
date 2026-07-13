import pdfplumber


def read_pdf(uploaded_file):

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"
                return text

    
from docx import Document


def read_docx(uploaded_file):

    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"
        return text
def extract_resume_text(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):

        return read_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):

        return read_docx(uploaded_file)

    return ""