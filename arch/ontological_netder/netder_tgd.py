from ontological_netder.netder_rule import NetDERRule

class NetDERTGD(NetDERRule):

	def __init__(self, rule_id, ont_body = [], net_body = [], ont_head = [], net_head = [], global_cond = []):
		super().__init__(rule_id, ont_body, net_body, ont_head, net_head, global_cond)