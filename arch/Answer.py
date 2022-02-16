class Answer:

	def __init__(self, basicAnswer, mapping=None):
		self._basicAnswer = basicAnswer
		if self._basicAnswer:
			self._mapping = mapping
		else:
			self._mapping = None

	def get_basic_answer(self):
		return self._basicAnswer

	def set_basic_answer(self, basicAnswer):
		self._basicAnswer = basicAnswer

	def get_mapping(self):
		return self._mapping

	def set_mapping(self, mapping):
		self._mapping = mapping