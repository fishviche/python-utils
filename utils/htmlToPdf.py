from xhtml2pdf import pisa
import jinja2


def create_html(html_text: str, html_name: str):
    """
    Function to create HTML
        html_text: HTML content
        html_name: HTML route(with name) or HTML name
        e.g: 'index.html' or '/home/root/index.html'
    """
    f = open(html_name, 'w')
    f.write(html_text)
    f.close()


def create_pdf(html_name: str, output_filename: str, info: dict):
    """
    Function to create PDF from HTML
        html_name: Complete file route (include file name) or HTML name
        output_filename: Output file name
        info: Dict with variables for jinja2
    """
    name_template = html_name.split('/')[-1]
    route_template = html_name.replace(name_template, "")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(route_template))
    template = env.get_template(name_template)
    html = template.render(info)
    result_file = open(output_filename, "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return pisa_status.err

if __name__ == "__main__":
    create_html('<h1>Hola</h1>', 'index.html')
    create_pdf('index.html', 'erick.pdf', {
        "resultados": "TU RESULTADO ES NEGATIVsssO",
        "test1": "PRobando"
        })
