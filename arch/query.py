from quantifier import Quantifier

class Query:

	def __init__(self, quantification, atoms):
		self._atoms = atoms
		self._quantification = quantification

	def get_atoms(self):
		return self._atoms

	def set_atoms(self, atoms):
		self._atoms = atoms

	def get_quantification(self):
		return self._quantification

	def set_quantification(self, quantification):
		self._quantification = quantification

	def get_variables(self):
		result = []
		for atom in self._atoms:
			for var in atom.get_variables():
					var_copy = copy.deepcopy(var)
					result.append(var_copy)

		return result

	def get_free_variables(self):
		result = []
		variables = self.get_variables()
		quantification = self._quantification
		exist_var = quantification[Quantifier.EXISTENTIAL]
		for var in variables:
			if not (var in exist_var):
				result.append(copy.deepcopy(var))
		return result


	def __str__(self):
		result = ''
		quantification = self._quantification
		exist_var = quantification[Quantifier.EXISTENTIAL]
		if len(exist_var) > 0:
			result = result + Quantifier.EXISTENTIAL
			for var in exist_var:
				result = result + var.getId() + ','
			#saco la coma que sobra
			result = result[:-1]
		
		result = result + '('

		for atom in self._atoms:
			result = result + str(atom) + '∧'

		#saco ∧ que sobra y agrego de perentesis de cierre
		result = result[:-1] + ')'

		return result