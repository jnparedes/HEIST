from atom import Atom

class Distinct(Atom):

	def __init__(self, value1, value2):
		super().__init__('distinct', [value1, value2])

	def is_mapped(self, atom):
		result = False
		result = (self._terms[0].isInstanced() and self._terms[1].isInstanced()) and (self._terms[0].getValue() != self._terms[1].getValue())
		result = result or (not (self._terms[0].isInstanced() and self._terms[1].isInstanced()) and self._id != atom.getId())
		return result

	def get_mapping(self, atom):
		return {}

	def __str__(self):
		return str(self._terms[0]) + ' ≠ ' + str(self._terms[1])