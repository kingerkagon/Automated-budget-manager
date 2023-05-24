from PyPDF2 import PdfReader

def read_pdf_document(pdf_path):
    """
    _summary_
    """
    reader = PdfReader(pdf_path)

    page = reader.pages[0]
    information = page.extract_text()
    lines = information.split("\n")

    prices = line_parser(lines)

    return prices

def line_parser(page_lines):
    """
    _summary_
    """
    prices = {}
    for line in page_lines:
        if "CARTE NUMERO" in line:
            price = line.split("805",1)[1]
            prices[line] = price
    return prices

if __name__ == '__main__':
    path = 'D:/Budget manager project/pdf files/releve_CCP1361399C030_20201204.pdf'
    prices = read_pdf_document(path)
    print(prices)