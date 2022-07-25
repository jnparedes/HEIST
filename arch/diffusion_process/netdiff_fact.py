from ontological_netder.net_comp_target import NetCompTarget
from constant import Constant

class NetDiffFact(NetCompTarget):
	ID = "net_diff_fact"
	def __init__(self, component, label, interval, t_lower, t_upper):
		super().__init__(component, label, interval)
		self._t_upper = t_upper
		self._t_lower = t_lower
		self._symbol = NetDiffFact.ID
		self._terms.append(Constant(self._t_lower))
		self._terms.append(Constant(self._t_upper))

	def getTimeUpper(self):
		return self._t_upper

	def getTimeLower(self):
		return self._t_lower

	def __str__(self):
		net_diff_dict = {}
		net_diff_dict["component"] = str(self._component)
		net_diff_dict["label"] = str(self._label)
		net_diff_dict["confidence"] = str(self._interval)
		net_diff_dict["time"] = '[' + str(self._t_lower) + ',' + str(self._t_upper) + ']'
		return str(net_diff_dict)