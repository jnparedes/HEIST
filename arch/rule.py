class Rule:

	def __init__(self, body, head):
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