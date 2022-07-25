import hashlib
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

	def __hash__(self):
		mystring = str(self._ID)
		mystring = mystring.encode('utf-8')
		return int(hashlib.sha1(mystring).hexdigest(), 16)

	def __str__(self):
		return str(self._ID)

	def isInstanced(self):
		return self._value != None

	def can_be_instanced(self):
		return not self.isInstanced()

	def __eq__(self, term):
		result = False
		if term is None:
			result = (self is term)
		else:
			result = (self._ID == term.get_id())

		return result