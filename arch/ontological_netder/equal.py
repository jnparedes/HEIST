from atom import Atom

class Equal(Atom):

	def __init__(self, value1, value2):
		super().__init__('equal', [value1, value2])
		self._pk_variable = None

	#se puede mapear a cualquier atomo si los dos terminos de este atomo estan instanciados y estos son iguales o
	#los terminos de este atomo no estan instanciados y el parametro "atom" tiene "id" diferente (osea no es "equal")
	def is_mapped(self, atom):
		result = False
		result = (self._terms[0].isInstanced() and self._terms[1].isInstanced()) and (self._terms[0].getValue() == self._terms[1].getValue())
		result = result or (not (self._terms[0].isInstanced() and self._terms[1].isInstanced()) and self._id != atom.getId())
		return result

	def get_mapping(self, atom):
		return {}

	def __str__(self):
		return str(self._terms[0]) + ' = ' + str(self._terms[1])

	def get_variables(self):
		result = []
		return result