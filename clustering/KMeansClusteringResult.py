from django.conf import settings

class Cluster:
	def __init__ (self,
								indxOfCluster = 0,
								wordList = [],
								itemCount = 0):
		self.indxOfCluster = indxOfCluster
		self.wordList = wordList
		self.itemCount = itemCount

	def show(self):
		print("Cluster no " + " " + str(self.indxOfCluster))
		print("Most common terms are: " + ''.join([i for i in self.wordList]))
		
class KMeansResults:
	def __init__(self,
							 fileName = ""):
		self.results = []
		self.fileName = fileName

	def add_cluster(self,
									indx,
									terms,
									itemCount):
		res = Cluster(indx, terms, itemCount)
		self.results.append(res)


		
