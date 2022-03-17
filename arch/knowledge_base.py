class KnowledgeBase:

	def __init__(self, rules, atoms):
		self._rules = rules
		self._atoms = atoms

	def getData(self):
		return self._atoms
	
	def getRules(self):
		return self._rules

