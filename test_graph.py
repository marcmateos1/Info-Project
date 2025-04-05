from graph import *



print("Probando el grafo...")
A= CreateGraph_1()
Plot(A)
PlotNode(A, "G")

# Probar GetClosest
n = GetClosest(A, 15, 5)
print(n.name)  # Debe imprimir "J"

n = GetClosest(A, 8, 19)
print(n.name)  # Debe imprimir "B"

A= CreateGraphFromFiles("ElsMeusNodesSegments.txt")
Plot(A)
PlotNode(A, "A")


print("Probando el grafo 2...")
Q= CreateGraph_2()
Plot(Q)
PlotNode(Q, "G")