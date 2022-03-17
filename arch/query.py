class Query:

	def __init__(self, quantification, terms):
		self._terms = terms
		self._quantification = quantification

	def get_terms(self):
		return self._terms

	def get_quantification(self):
		return self._quantification
