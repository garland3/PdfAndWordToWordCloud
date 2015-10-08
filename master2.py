import os, sys

from docx import opendocx, getdocumenttext

def wordToText(path):
	temp = os.path.splitext(path)
	print path
	inputFile = path
	outputFile = temp[0] +"1.txt"
	print outputFile
	#inputFile = os.path.abspath(inputFile)
	print inputFile

	try:
		document = opendocx(inputFile)
		newfile = open(outputFile, 'w')
	except:
		print(
		"Please supply an input and output file. For example:\n"
		"  example-extracttext.py 'My Office 2007 document.docx' 'outp"
		"utfile.txt'"
		)
		exit()

	# Fetch all the text out of the document we just created
	paratextlist = getdocumenttext(document)
	#print paratextlist

	# Make explicit unicode version
	newparatextlist = []
	for paratext in paratextlist:
		newparatextlist.append(paratext.encode("utf-8"))
		#print paratext

	# Print out text of document with two newlines under each paragraph
	newfile.write('\n\n'.join(newparatextlist))


# Open a file
path = "./"
dirs = os.listdir( path )

# This would print all the files and directories
for file1 in dirs:
	# print file
	temp = os.path.splitext(file1)
	if(temp[1]  =='.doc' or temp[1]  =='.docx'):
		#print temp
		#print file1
		wordToText(file1)
		