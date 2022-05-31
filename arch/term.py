class Term:
	
	def __init__(self, id_term, value):
		self._ID = id_term
		self._value = value

	def get_id(self):
		return self._ID

	def get_value(self):
		return self._value

	def set_value(self, value):
		self._value = value
