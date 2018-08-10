import os
import nltk
import random
from sklearn.externals import joblib
from nltk.corpus.reader import CategorizedTaggedCorpusReader

class NBCategoryPredictor:
	def __init__( self,
								corpusPath,
								word_features = []):
		self.corpusPath = corpusPath
		os.chdir(corpusPath)

	def document_features(self, document):
		document_words = set(document)
		features = {}
		for word in self.word_features:
			features['contains({})'.format(word)] = (word in document_words)
		return features
    									
	def create_model(self):
		corpus_root = self.corpusPath
		reader = CategorizedTaggedCorpusReader( corpus_root, r'.*', cat_file = "cats.txt" )

		documents = [(list(reader.words(fileid)), category)
									for category in reader.categories()
									for fileid in reader.fileids(category)]
		random.shuffle(documents)

		all_words = nltk.FreqDist(w.lower() for w in reader.words())
		self.word_features = list(all_words)[:2000]
		featuresets = [(self.document_features(d), c) for (d, c) in documents]
		NBClassifier = nltk.NaiveBayesClassifier.train(featuresets)

		joblib.dump(NBClassifier,  'NBClassifier.pkl')
		#classifier.show_most_informative_features(15)
		# To Test Classifier
		#print(nltk.classify.accuracy(NBClassifier, featuresets))

		#print(classifier.classify(document_features('Description for ticket to categorizes!')))
