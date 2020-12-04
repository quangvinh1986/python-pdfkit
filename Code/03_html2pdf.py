import pdfkit

def html2pdf(html_file_name, pdf_file_name):
    options = {'encoding': "UTF-8"}
    pdfkit.from_file(html_file_name, pdf_file_name, options=options)


if __name__ == "__main__":
    html2pdf("demo.html", "demo_unicode.pdf")
