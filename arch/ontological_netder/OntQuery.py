import copy
class OntQuery:

	def __init__(self, exist_var = [], ont_cond = []):
		self._exist_var = exist_var
		self._ont_cond = ont_cond

	def get_exist_var(self):
		return self._exist_var

	def get_ont_body(self):
		return self._ont_cond

	def get_variables(self):
		result = []
		for atom in self._ont_cond:
			for var in atom.get_variables():
					var_copy = copy.deepcopy(var)
					result.append(var_copy)

		return result

	def get_free_variables(self):
		result = []
		variables = self.get_variables()
		exist_var = self.get_exist_var()
		for var in variables:
			if not (var in exist_var):
				result.append(copy.deepcopy(var))
		return result


	def __str__(self):
		result = ''
		if len(self._exist_var) > 0:
			result = result + '∃'
			for var in self._exist_var:
				result = result + var.getId() + ','
			#saco la coma que sobra
			result = result[:-1]
		
		result = result + '('

		for atom in self._ont_cond:
			result = result + str(atom) + '∧'

		#saco ∧ que sobra y agrego de perentesis de cierre
		result = result[:-1] + ')'

		return result


