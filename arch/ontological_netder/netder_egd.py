from Ontological.NetDERRule import NetDERRule

class NetDEREGD(NetDERRule):

	def __init__(self, rule_id, ont_body = [], net_body = [], head = [], global_cond = []):
		super().__init__(rule_id = rule_id, ont_body = ont_body, net_body = net_body, ont_head = head, global_cond= global_cond)