import pdfkit

urls = ["https://www.google.com/search?q=codelearn.io", "https://www.google.com/search?q=codelearn.io+%2B+quangvinh1986",
        "https://www.google.com/search?q=codelearn.io+python"]
pdfkit.from_url(urls, "multi_codelearn.pdf")