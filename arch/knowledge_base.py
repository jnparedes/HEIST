class KnowledgeBase:

	def __init__(self, rules, atoms):
		self._rules = rules
		self._atoms = atoms

	def get_data(self):
		return self._atoms
	
	def set_data(self, atoms):
		self._atoms = atoms

	def get_rules(self):
		return self._rules

	def set_rules(self, rules):
		self._rules = rules
