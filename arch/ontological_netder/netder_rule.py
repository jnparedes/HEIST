from rule import Rule

class NetDERRule(Rule):

	def __init__(self, rule_id, ont_body=[], net_body=[], ont_head = [], net_head = [], global_cond=[]):
		body = {"ont_body": ont_body, "net_body": net_body}
		head = {"ont_head": ont_head, "net_head": net_head}
		super().__init__(rule_id, body, head)
		self._global_cond = global_cond

	def get_global_cond(self):
		return self._global_cond

	def set_global_cond(self, global_cond):
		self._global_cond = global_cond

	def get_ont_head(self):
		return self._head["ont_head"]

	def get_net_head(self):
		return self._head["net_head"]