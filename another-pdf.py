#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-
# https://chirale.wordpress.com/2013/05/10/create-nice-unicode-pdf-using-python/
from fpdf import FPDF
import json
import urllib2
import os
import cgi
import sys
# set system encoding to unicode
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# e.g. http://example.com/cgi-bin/myscript.py?lang=en&sid=2
sid = arguments.getlist('sid')[0]
lang = arguments.getlist('lang')[0]

# compile a request to get a particular element from an external json
dataurl = "http://example.com/external-json-source?lang=%s&sid=%s" % (lang, sid)

# load json from dataurl and convert into python elements
data = json.load(urllib2.urlopen(dataurl))

# the json has a user attribute: the user attribute has name and surname attributes as strings
user = data['user']

# title is a simple string
title = data['title']
lato_lungo = 297
lato_corto = 210
pdf = FPDF('L','mm','A4')

# add unicode font
pdf.add_font('DejaVu','','DejaVuSansCondensed.ttf',uni=True)
pdf.add_page()
pdf.cell(w=lato_lungo,h=9,txt=title,border=0,ln=1,align='L',fill=0)
pdf.set_font('DejaVu','',12)

# paragraphs rendered as MultiCell
# @see https://code.google.com/p/pyfpdf/wiki/MultiCell
# print key: values for each user['data'] dictionary attributes
for val in user.iteritems():
    pdf.multi_cell(w=0,h=5,txt="%s: %s" % val)
# finally print pdf
print pdf.output(dest='S')
