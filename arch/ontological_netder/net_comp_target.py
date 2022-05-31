import os, sys
import portion
from atom import Atom
from constant import Constant

class NetCompTarget(Atom):
	ID = "net_comp_target"

	def __init__(self, component, label, interval):
		terms = [Constant(str(hash(component))), Constant(label), Constant(interval.lower), Constant(interval.upper)]
		super().__init__(NetCompTarget.ID, terms)
		self._component = component
		self._label = label

	def getBound(self):
		return portion.closed(self._terms[2].get_value(), self._terms[3].get_value())

	def getLabel(self):
		return self._label

	def getComponent(self):
		return self._component