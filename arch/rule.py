class Rule:

	def __init__(self, rule_id, body, head):
		self._id = rule_id
		self._body = body
		self._head = head

	def get_body(self):
		return self._body

	def set_body(self, body):
		self._body = body

	def get_head(self, head):
		return self._head

	def set_head(self, head):
		self._head = head

	def get_id(self):
		return self._id

	def set_id(self, id_rule):
		self._id = id_rule