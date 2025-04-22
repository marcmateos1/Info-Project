from graph import*
from node import*
C=Path()

AddNodeToPath(C,Node("A", 1, 20))
AddNodeToPath(C,Node("B", 8, 17))
AddNodeToPath(C,Node("C", 15, 20))
AddNodeToPath(C,Node("D", 18, 15))
#AddNodeToPath(C,Node("L", 4, 10))

G=CreateGraph_1()

print(get_node_by_name(G,"B"))
print(G.nodes[1].name)
print(ReachableNodes(G,"B"))
PlotPath(G,C)
n1=Node("A", 1, 20)
n2=Node("C", 15, 20)
#FindShortestPath(G,n1,n2 )