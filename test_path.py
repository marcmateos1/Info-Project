from graph import*
from node import*
from path import CostToNode

C=Path()

AddNodeToPath(C,Node("A", 1, 20))
AddNodeToPath(C,Node("B", 8, 17))
AddNodeToPath(C,Node("C", 15, 20))
AddNodeToPath(C,Node("D", 18, 15))
#AddNodeToPath(C,Node("L", 4, 10))

G=CreateGraph_1()


#print(get_node_by_name(G,"B"))
#print(G.nodes[1].name)
#print(ReachableNodes(G,"B"))
#PlotPath(G,C)
#n1=Node("D", 1, 20)
#n2=Node("E", 10, 3)
#print(G.nodes[0].list_of_neighbours)
#l=FindShortestPath(G,n1,n2 )
#PlotPath(G,l)
#print(CostToNode(l,n2))

#print(Reachability(G,"A"))
n=Reachability(G, "F")
Plot_All_Paths(G,n)