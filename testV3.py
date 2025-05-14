from airSpace import*
#print("Hola1")
g=AirSpace()
LoadNavPoints("cat_nav", g)
LoadNavSegments("cat_seg.txt", g)
LoadNavAirports("cat_aer.txt", g)
#print("Hola2")

#PlotMap(g)
#NeighboursMap(g, "GODOX")

cami=FindShortestMap(g, "GODOX", "ANTON")
PlotShortestPath(g, cami)