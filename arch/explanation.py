from abc import ABC, abstractmethod
class Explanation(ABC):

	@abstractmethod
	def show(self):
		pass