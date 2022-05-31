from af_netdiff_fact import AFNetDiffFact
import portion
from n_local_label import NLocalLabel

class CFNetDiffFactRedLabels(AFNetDiffFact):

	def __init__(self, net_diff_graph, tmax):
		super().__init__(net_diff_graph.getNodes(), [NLocalLabel('red')], [portion.closed(1,1)], [(0,tmax)])
