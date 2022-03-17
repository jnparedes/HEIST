from Atom import Atom
class Entity(Atom):

	def __init__(self, value, symbol, terms):
		super().__init__(symbol, terms)
		self._value = value


	def get_value(self):
		return self._value