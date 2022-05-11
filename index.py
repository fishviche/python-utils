from utils.htmlToPdf import create_html, create_pdf
html_content = '<h1>Hola</h1>'
html_name = 'index.html'
pdf_name = 'erick.pdf'
pdf_content = {
    "resultados": "TU RESULTADO ES NEGATIVsssO",
    "test1": "PRobando"
    }
create_html(html_content, html_name)
create_pdf(html_name, pdf_name, pdf_content)
