from airSpace import*

g=AirSpace()
LoadNavAirports("cat_aer.txt", g)
LoadNavSegments("cat_seg.txt", g)
LoadNavPoints("cat_nav", g)

PlotCat(g)