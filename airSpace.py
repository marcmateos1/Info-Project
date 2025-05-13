from navAirpoint import NavAirport
from navPoint import NavPoint
from navSegment import NavSegment
import matplotlib.pyplot as plt


class AirSpace:
    def __init__(self):
        self.list_navpoints=[]
        self.list_navsegments=[]
        self.list_navairports=[]

def LoadNavPoints(file, airspace):
    F=open(file, "r")
    line=F.readline()
    while line!="":
        trozos=line.rstrip().split()
        navpoint=NavPoint(trozos[0], trozos[1], trozos[2], trozos[3])
        airspace.list_navpoints.append(navpoint)
        line=F.readline()
    F.close()

def LoadNavSegments(file, airspace):
    F = open(file, "r")
    line = F.readline()
    while line != "":
        trozos = line.rstrip().split()
        navseg = NavSegment(trozos[0], trozos[1], trozos[2])
        airspace.list_navsegments.append(navseg)
        line=F.readline()
    F.close()

def LoadNavAirports(file,airspace):
    with open(file, "r") as F:
        lines = F.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("LE") and len(line) == 4:
            nom = line
            sids = []
            stars = []
            i += 1
            while i < len(lines) and not (lines[i].strip().startswith("LE") and len(lines[i].strip()) == 4):
                current = lines[i].strip()
                if current.endswith(".D"):
                    sids.append(current)
                elif current.endswith(".A"):
                    stars.append(current)
                i += 1
            airspace.list_navairports.append(NavAirport(nom, sids, stars))
        else:
            i += 1

def PlotMap(airspace):
    for navpoint in airspace.list_navpoints:
        plt.scatter(navpoint.longitud, navpoint.latitud, color="blue", s=10)
        plt.text(navpoint.longitud, navpoint.latitud, navpoint.name, fontsize=6, color="black")

    for segment in airspace.list_navsegments:

        found_origin=False
        found_dest=False

        for navpoints in airspace.list_navpoints:
            if navpoints.number==segment.originnumber:
                originnav=navpoints
                found_origin=True

            elif navpoints.number==segment.destnumber:
                destnav=navpoints
                found_dest=True

            elif found_dest==True and found_origin==True:
                break

        longitud_values=[originnav.longitud, destnav.longitud]
        latitud_values=[originnav.latitud, destnav.latitud]
        plt.plot(longitud_values, latitud_values, color="purple", linewidth=1)

        mid_x = (originnav.longitud + destnav.longitud) / 2
        mid_y = (originnav.latitud + destnav.latitud) / 2
        plt.text(mid_x, mid_y, f"{segment.distance:.2f}", fontsize=5, color="black")

        dx=destnav.longitud-originnav.longitud
        dy=destnav.latitud-originnav.latitud
        scale=0.95
        plt.arrow(originnav.longitud, originnav.latitud, dx*scale, dy*scale, length_includes_head=True, head_width=0.02, head_length=0.02, fc="purple", ec="purple", linewidth=0.5)



    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Mapa Espai Aeri")
    plt.grid()
    plt.show()

def NeighboursMap(airspace, origen):
    nav_buscat=None
    for navpoint in airspace.list_navpoints:
        if navpoint.name==origen:
            nav_buscat=navpoint
            break
    if nav_buscat==None:
        return None

    for navpoint in airspace.list_navpoints:
        plt.scatter(navpoint.longitud, navpoint.latitud, color="grey", s=10)
        plt.text(navpoint.longitud, navpoint.latitud, navpoint.name, fontsize=6, color="black")


    plt.scatter(nav_buscat.longitud, nav_buscat.latitud, color="blue", s=10)

    for segment in airspace.list_navsegments:

        found_origin=False
        found_dest=False

        for navpoints in airspace.list_navpoints:
            if navpoints.number==segment.originnumber:
                originnav=navpoints
                found_origin=True

            elif navpoints.number==segment.destnumber:
                destnav=navpoints
                found_dest=True

            elif found_dest==True and found_origin==True:
                break

        if originnav==nav_buscat:
            longitud_values = [originnav.longitud, destnav.longitud]
            latitud_values = [originnav.latitud, destnav.latitud]
            plt.plot(longitud_values, latitud_values, color="purple", linewidth=1)

            mid_x = (originnav.longitud + destnav.longitud) / 2
            mid_y = (originnav.latitud + destnav.latitud) / 2
            plt.text(mid_x, mid_y, f"{segment.distance:.2f}", fontsize=5, color="black")

            dx = destnav.longitud - originnav.longitud
            dy = destnav.latitud - originnav.latitud
            scale = 0.95
            plt.arrow(originnav.longitud, originnav.latitud, dx * scale, dy * scale, length_includes_head=True,
                      head_width=0.02, head_length=0.02, fc="purple", ec="purple",)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Mapa Espai Aeri -- Veïns de {origen}")
    plt.grid()
    plt.show()