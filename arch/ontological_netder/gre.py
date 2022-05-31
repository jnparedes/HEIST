import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from atom import Atom
class GRE(Atom):

	def __init__(self, value1, value2):
		super().__init__('gre', [value1, value2])
		self._pk_variable = None

	def is_mapped(self, atom):
		result = False
		result = self._terms[0].getId() >= self._terms[1].getId()
		return result

	def get_mapping(self, atom):
		return {}

	def __str__(self):
		return str(self._terms[0]) + ' ≥ ' + str(self._terms[1])

	def get_variables(self):
		result = []
		return result
