from abc import ABC, abstractmethod
class Style(ABC):

	@abstractmethod
	def explain(self, answer, query):
		pass
