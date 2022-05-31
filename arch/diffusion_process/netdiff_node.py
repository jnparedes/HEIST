import random
from diffusion_process.netdiff_graph_element import NetDiffGraphElement

class NetDiffNode(NetDiffGraphElement):

	def __init__(self, id):
		self._id = id
		self._color = "blue"

	def get_labels(self):
		return NetDiffNode._labels

	def __str__(self):
		return 'node(' + self._id + ')'

	def __hash__(self):
		return hash(str(self))

	def to_json_string(self):
		return '{"id":"' + str(self._id) + '", "label": "' + str(self._id) + '", "color": "' + self._color + '" }'

	def set_color(self, color):
		self._color = color

	def get_color(self):
		return self._color

	def getId(self):
		return self._id

	def __eq__(self, node):
		result = False
		if isinstance(self, type(node)):
			result = self is node

			result = result or (self._id == node.getId())

		return result