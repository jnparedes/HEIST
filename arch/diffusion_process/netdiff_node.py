import random
from diffusion_process.netdiff_graph_element import NetDiffGraphElement
from constant import Constant

class NetDiffNode(NetDiffGraphElement):
	ID = "node"
	
	def __init__(self, id):
		self._id = id
		super().__init__("node", [Constant(str(id))])

	def get_labels(self):
		return NetDiffNode._labels

	def __hash__(self):
		return NetDiffGraphElement.__hash__(self)

	def to_json_string(self):
		return '{"id":"' + str(self._id) + '", "label": "' + str(self._id) + '" }'

	def getId(self):
		return self._id

	def __eq__(self, node):
		result = False
		if isinstance(self, type(node)):
			result = self is node

			result = result or (self._id == node.getId())

		return result