import pdfkit

def text2pdf(message, file_name):
    options = {'encoding': "UTF-8"}
    pdfkit.from_string(message, file_name, options=options)


if __name__ == "__main__":
    message = "Đây là thông điệp từ tác giả bài viết trên codelearn"
    text2pdf(message, "message_vi_unicode.pdf")
