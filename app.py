html = """
<H1 align="center">html2fpdf</H1>
<h2>Basic usage</h2>
<p>You can now easily print text while mixing different
styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
<B><I><U>all at once</U></I></B>!
 
<BR>You can also insert hyperlinks
like this <A HREF="http://www.mousevspython.com">www.mousevspython.comg</A>,
or include a hyperlink in an image. Just click on the one below.<br>
<center>
<A HREF="http://www.mousevspython.com"><img src="tutorial/logo.png" width="150" height="150"></A>
</center>
 
<h3>Sample List</h3>
<ul><li>option 1</li>
<ol><li>option 2</li></ol>
<li>option 3</li></ul>
 
<table border="0" align="center" width="50%">
<thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
<tbody>
<tr><td>cell 1</td><td>cell 2</td></tr>
<tr><td>cell 2</td><td>cell 3</td></tr>
</tbody>
</table>
"""

#!flask/bin/python
import PyPDF2
import os

from flask import Flask
from flask import jsonify
from flask import send_from_directory
#from flask import abort
#from flask import make_response
from flask import request
from pyfpdf import FPDF, HTMLMixin

app = Flask(__name__)  

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = '/static/pdfs'

reports = [
    {
        'id': 1,
        'report_type': u'Relatório Temperatura Umidade',
        'report_desc': u'Temperatura e Umidade mensal', 
        'sensor_name': u'sala_atto',
        'sensor_id': u'432432',
        'events': [
            {
                event: u'XXXXX', 
                timestamp: u'1471808276'
            },
            {
                event: u'XXXXX', 
                timestamp: u'1471808332'
            }
        ],
        'url_image': u'http://someurl.com',
        'measure_min': u'150',
        'measure_max': u'450'
    },
    {
        'id': 2,
        'report_type': u'Relatório Temperatura Umidade',
        'report_desc': u'Temperatura e Umidade mensal', 
        'sensor_name': u'sala_atto',
        'sensor_id': u'432432',
        'events': [
            {
                event: u'XXXXX', 
                timestamp: u'1471808276'
            },
            {
                event: u'XXXXX', 
                timestamp: u'1471808332'
            }
        ],
        'url_image': u'http://someurl.com',
        'measure_min': u'150',
        'measure_max': u'450'
    }
]

@app.route('/')
def index():
    return "API REST Reports Digite no seu navegador: http://127.0.0.1:5000/api/v1/pdfs/2.pdf para retornar o pdf de nome 2.pdf"


@app.route('/api/v1/pdfs/<filename>')  
def send_file(filename):  
    # if path is None:
    #     abort(404)
    # files = os.listdir(path)
    # if not files:
    #     abort(404)
    # return send_from_directory(path, files[0])
    return send_from_directory(BASE_DIR + UPLOAD_FOLDER, filename)

@app.route('/api/v1/reports', methods=['POST'])
def prepare_json():
    if not request.json or not 'report' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'username': request.json['username'],
        'email': request.json['email'],
        'name': request.json['name'],
        'cpf': request.json['cpf'],
        'rg': request.json['rg'],
        'phone': request.json['phone']
    }

    users.append(user)
    
    return jsonify({'user': user}), 201

def create_pdf():
    response.title = "web2py sample listing"

    # define header and footers:
    head = THEAD(TR(TH("Header 1", _width="50%"), 
                    TH("Header 2", _width="30%"),
                    TH("Header 3", _width="20%"), 
                    _bgcolor="#A0A0A0"))
    foot = TFOOT(TR(TH("Footer 1", _width="50%"), 
                    TH("Footer 2", _width="30%"),
                    TH("Footer 3", _width="20%"),
                    _bgcolor="#E0E0E0"))

    # create several rows:
    rows = []
    for i in range(1000):
        col = i % 2 and "#F0F0F0" or "#FFFFFF"
        rows.append(TR(TD("Row %s" %i),
                       TD("something", _align="center"),
                       TD("%s" % i, _align="right"),
                       _bgcolor=col)) 

    # make the table object
    body = TBODY(*rows)
    table = TABLE(*[head, foot, body], 
                  _border="1", _align="center", _width="100%")

    pdf = MyFPDF()
    # first page:
    pdf.add_page()
    pdf.write_html(str(XML(table, sanitize=False)))
    response.headers['Content-Type'] = 'application/pdf'
    return pdf.output(dest='S')

# Cria o pdf padrão de acordo com a biblioteca pyFPDF 
class MyFPDF(FPDF, HTMLMixin):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, response.title, 1, 0, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        txt = 'Page %s of %s' % (self.page_no(), self.alias_nb_pages())
        self.cell(0, 10, txt, 0, 0, 'C')

if __name__ == '__main__':
    app.run(debug=True)