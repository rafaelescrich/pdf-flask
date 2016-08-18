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
 
from pyfpdf import FPDF, HTMLMixin
 
class MyFPDF(FPDF, HTMLMixin):
    pass
 
pdf=MyFPDF()
#First page
pdf.add_page()
pdf.write_html(html)
pdf.output('html.pdf','F')

#another implementation

from xhtml2pdf import pisa
from StringIO import StringIO

def create_pdf(pdf_data):
    pdf = StringIO()
    pisa.CreatePDF(StringIO(pdf_data), pdf)
    return pdf

import os
from flask import Flask, request, redirect, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp/'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    <p>%s</p>
    """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

if __name__ == "__main__":
app.run(host='0.0.0.0', port=5001, debug=True)