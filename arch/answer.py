class Answer:

	def __init__(self, basicAnswer, mapping=None):
		self._basicAnswer = basicAnswer
		if not self._basicAnswer:
			self._mapping = None
		else:
			self._mapping = mapping

	def get_basic_answer(self):
		return self._basicAnswer

	def set_answer(self, basicAnswer, mapping = None):
		self._basicAnswer = basicAnswer
		if not self._basicAnswer:
			self._mapping = None
		else:
			self._mapping = mapping


	def get_mappings(self):
		return self._mapping