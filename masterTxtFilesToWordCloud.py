import os
from wordcloud import WordCloud


# text = open(path.join(d, 'SIMP.txt')).read()
# Read the whole text.

def makeWorldCloud(path1):
	
	temp = os.path.splitext(path1)
	outputFile = temp[0] +".png"
	print outputFile
	
	
	text = open(path1).read()

	# Generate a word cloud image
	wordcloud = WordCloud().generate(text)

	# Display the generated image:
	# the matplotlib way:
	import matplotlib.pyplot as plt
	plt.imshow(wordcloud)
	plt.axis("off")

	# take relative word frequencies into account, lower max_font_size
	wordcloud = WordCloud(max_font_size=40).generate(text)
	plt.figure()
	plt.imshow(wordcloud)
	plt.axis("off")
	#plt.show()
	plt.savefig(outputFile)
	
# Open a file
d = os.path.dirname(__file__)
dirs = os.listdir( d )

# This would print all the files and directories
for file1 in dirs:
	# print file
	temp = os.path.splitext(file1)
	if(temp[1]  =='.txt'):
		#print temp
		#print file1
		makeWorldCloud(file1)