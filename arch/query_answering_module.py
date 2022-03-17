from abc import ABC
class QueryAnsweringModule(ABC):

	def __init__(self, user, symbolic):
		self._user = user
		self._symbolic = symbolic

	@abstractmethod
	def answer_query(self, query):
		pass

	def get_sources(self):
		self._symbolic.get_sources()
