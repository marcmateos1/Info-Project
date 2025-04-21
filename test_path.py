from graph import CreateGraph_1
from path import *
from node import*
C=Path()
AddNodeToPath(C,Node("A", 1, 20))
AddNodeToPath(C,Node("B", 8, 17))
AddNodeToPath(C,Node("C", 15, 20))
AddNodeToPath(C,Node("K", 3, 15))
G=CreateGraph_1()

PlotPath(G,C)