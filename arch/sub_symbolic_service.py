from abc import ABC, abstractmethod
class Sub-symbolicService(ABC):

	def __init__(self, location):
		self._service_location = location

	@abstractmethod
	def train(self, entities):
		pass

	@abstractmethod
	def invoke(self, entity):
		pass
