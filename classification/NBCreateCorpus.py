import pandas
import os
import nltk
from django.conf import settings

class NBCreateCorpus:
	def __init__(	self, 
								fileName = "",
								sheetName = ""):
		self.fileName = fileName
		self.sheetName = sheetName
		
	def create_corpus(self):
		df = pandas.read_excel(self.fileName, self.sheetName)
		catFileMap = {}
		c = 97
		d = 97
		for i in df.index:
			if len(str(df['Category 1'][i]))>0:
				cat_temp = df['Category 1'][i]
			else:
				cat_temp = "NOCAT"
			if cat_temp not in catFileMap:
				temp = chr(c) + chr(d)
				catFileMap[cat_temp] = "c" + temp
				d = d + 1
				if d > 122:
					c = c + 1
					d = 97
		print(catFileMap.values())
		print(catFileMap.keys())

		# To Create Corpus Files
		print("site root: " + settings.SITE_ROOT)
		os.chdir(settings.SITE_ROOT)
		print(os.path.realpath('./'))
		path = '../classification/NB_temp'
		os.chdir(path)
		os.mkdir(self.fileName.name)
		path = './' + self.fileName.name
		os.chdir(path)
		cats = open("cats.txt", "wt+", encoding='utf-8')

		catFileNames = {}
		for i in df.index:
			#print("saurabh " + str(i))
			if len(str(df['Category 1'][i]))>0:
				cat_temp = df['Category 1'][i]
			else:
				cat_temp = "NOCAT"
			val = catFileMap.get(cat_temp)
			if val not in catFileNames:
				catFileNames[val] = str(1).zfill(4)
			else:
				temp_int = int(catFileNames.get(val))
				temp_int = temp_int + 1
				catFileNames[val] = str(temp_int).zfill(4)

			content_text = nltk.word_tokenize("%s"% df['Description'][i])
			content_text = nltk.pos_tag(content_text)
			content_text = ' '.join([nltk.tag.tuple2str(tup) for tup in content_text])
			
			temp_file = val + catFileNames.get(val)
			f = open(temp_file, 'w', encoding= 'utf-8')
			f.write(content_text)
			f.close()
			cats.write(temp_file + ' ' + str(cat_temp).replace(' ', '_') + '\n')

		cats.close()
		corpusPath = os.path.realpath('./')
		os.chdir(settings.SITE_ROOT)
		return corpusPath
