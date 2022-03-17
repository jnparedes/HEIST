from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')

class Source(Generic[T], ABC):

	def __init__(self, knowledge):
		self._knowledge = knowledge

	@abstractmethod
	def accept(self, style_visitor_factory):
		pass

	@abstractmethod
	def create(self):
		pass