from graph import CreateGraph_1
from path import *
from node import*
C=Path()

AddNodeToPath(C,Node("A", 1, 20))
AddNodeToPath(C,Node("B", 8, 17))
AddNodeToPath(C,Node("C", 15, 20))
AddNodeToPath(C,Node("F", 15, 20))
AddNodeToPath(C,Node("L", 15, 20))

G=CreateGraph_1()

print(get_node_by_name(G,"B"))
print(G.nodes[1].name)
print(ReachableNodes(G,"B"))