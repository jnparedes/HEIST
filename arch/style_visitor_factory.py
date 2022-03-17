from abc import ABC
class StyleVisitorFactory(ABC):

	def __init__(self):
		self._style = None