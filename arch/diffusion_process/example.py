import sys
sys.path.append('../')
from diffusion_process.netdiff_program import NetDiffProgram
from diffusion_process.netdiff_fact import NetDiffFact
from diffusion_process.netdiff_local_rule import NetDiffLocalRule
from diffusion_process.tipping import Tipping
from diffusion_process.netdiff_graph import NetDiffGraph
from diffusion_process.netdiff_node import NetDiffNode
from diffusion_process.netdiff_edge import NetDiffEdge
from diffusion_process.label import Label
from diffusion_process.e_local_label import ELocalLabel
from diffusion_process.n_local_label import NLocalLabel
import portion
import networkx as nx

#max time for diffusion process
tmax = 2

#list of ids representing the nodes in the graph
nodes = ['0', '1', '2', '3']
#list of tuples representing the edges in the graph
edges = [('0', '1'), ('2', '1'), ('2', '3')]

#three labels that can be applied to the nodes
blue = NLocalLabel('blue')
yellow = NLocalLabel('yellow')
red = NLocalLabel('red')


nllabels = [blue, yellow, red]

#nllabels is assigned as the set of labels that can be applied to the nodes
NetDiffNode._labels = nllabels
#the set of labels that can be applied to the edges is empty
NetDiffEdge._labels = []

#NetDiffGraph is an extension of a networkx graph
graph = NetDiffGraph('graph', nodes, edges)
net_diff_node = list(graph.nodes)

#mancalog rule that says "red nodes that are blue with confidence between 0.5 and 1
#will be influenced next time by neighbors that are yellow with confidence between 0.5 and 1 according to function Tipping"
local_rule1 = NetDiffLocalRule(red, [(blue, portion.closed(0.5,1))], 1,[(yellow, portion.closed(0.5, 1))], None, Tipping(0.5, portion.closed(0.7, 1)))
#mancalog rule that says "blue nodes that are red with confidence between 0.7 and 1
#will be influenced next time by neighbors that are yellow with confidence between 0.5 and 1 according to function Tipping"
local_rule2 = NetDiffLocalRule(blue, [(red, portion.closed(0.7,1))], 1,[(yellow, portion.closed(0.5, 1))], None, Tipping(0.5, portion.closed(0.7, 1)))

local_rules = [local_rule2, local_rule1]


#mancalog fact that says "node 1 is blue with confidence interval [0.5, 1] at time [0, tmax]"
net_diff_fact1 = NetDiffFact(net_diff_node[1], blue, portion.closed(0.5, 1), 0, tmax)
#mancalog fact that says "node 0 is yellow with confidence interval [0.5, 1] at time [0, tmax]"
net_diff_fact2 = NetDiffFact(net_diff_node[0], yellow, portion.closed(0.5, 1), 0, tmax)
#mancalog fact that says "node 2 is yellow with confidence interval [0.7, 1] at time [0, tmax]"
net_diff_fact3 = NetDiffFact(net_diff_node[2], yellow, portion.closed(0.7, 1), 0, tmax)
facts = [net_diff_fact1, net_diff_fact2, net_diff_fact3]


program = NetDiffProgram(graph, tmax, facts, local_rules)

#mancalog interpretation that contains the final bounds for each label in each node and edge
interp = program.diffusion()

print(str(interp))