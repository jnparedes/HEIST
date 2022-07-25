from abc import ABC, abstractmethod
from diffusion_process.netdiff_world import NetDiffWorld
from atom import Atom

class NetDiffGraphElement(Atom, ABC):
	_labels = []

	def __init__(self, id, terms):
		super().__init__(id, terms)

	@abstractmethod
	def get_labels(self):
		pass

	def equals(self, element):
		return isinstance(element, type(self)) and self._symbol == element.get_symbol()

	def getInitialWorld(self):
		return NetDiffWorld(self.get_labels())

	def __hash__(self):
		return Atom.__hash__(self)