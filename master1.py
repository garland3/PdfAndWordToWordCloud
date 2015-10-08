import os, sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


def convert_pdf_to_txt(path):
	
	temp = os.path.splitext(path)
	
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
	fp = file(path, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	password = ""
	maxpages = 0
	caching = True
	pagenos=set()

	for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
		interpreter.process_page(page)

	text = retstr.getvalue()

	fp.close()
	device.close()
	retstr.close()
	
	outputFile = temp[0] +".txt"
	print outputFile
	
	ff = open(outputFile,'w')
	ff.write(text)
	ff.close()
    # return text
	
	






# Open a file
path = "./"
dirs = os.listdir( path )

# This would print all the files and directories
for file1 in dirs:
	# print file
	temp = os.path.splitext(file1)
	if(temp[1]  =='.pdf'):
		print temp
		print file1
		convert_pdf_to_txt(file1)
		

		