from abc import ABC, abstractmethod
class ReasoningTask(ABC):

	def __init__(self, sources, kb):
		self._sources = sources
		self._kb = kb

	@abstractmethod
	def answer_query(self, query):
		pass

	def get_sources(self):
		return self._sources
