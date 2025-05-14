from navAirpoint import NavAirport
from navPoint import NavPoint
from navSegment import NavSegment
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


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
    fig=Figure()
    ax=fig.add_subplot(111)
    for navpoint in airspace.list_navpoints:
        ax.scatter(navpoint.longitud, navpoint.latitud, color="blue", s=10)
        ax.text(navpoint.longitud, navpoint.latitud, navpoint.name, fontsize=6, color="black")

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
        ax.text(mid_x, mid_y, f"{segment.distance:.2f}", fontsize=5, color="black")

        dx=destnav.longitud-originnav.longitud
        dy=destnav.latitud-originnav.latitud
        scale=0.95
        ax.arrow(originnav.longitud, originnav.latitud, dx*scale, dy*scale, length_includes_head=True, head_width=0.02, head_length=0.02, fc="purple", ec="purple", linewidth=0.5)



    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Mapa Espai Aeri")
    ax.grid(True)

    return fig

def NeighboursMap(airspace, origen):
    fig=Figure()
    ax=fig.add_subplot(111)
    nav_buscat=None
    for navpoint in airspace.list_navpoints:
        if navpoint.name==origen:
            nav_buscat=navpoint
            break
    if nav_buscat==None:
        return None

    for navpoint in airspace.list_navpoints:
        ax.scatter(navpoint.longitud, navpoint.latitud, color="grey", s=10)
        ax.text(navpoint.longitud, navpoint.latitud, navpoint.name, fontsize=6, color="black")


    ax.scatter(nav_buscat.longitud, nav_buscat.latitud, color="blue", s=10)

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
            ax.plot(longitud_values, latitud_values, color="purple", linewidth=1)

            mid_x = (originnav.longitud + destnav.longitud) / 2
            mid_y = (originnav.latitud + destnav.latitud) / 2
            ax.text(mid_x, mid_y, f"{segment.distance:.2f}", fontsize=5, color="black")

            dx = destnav.longitud - originnav.longitud
            dy = destnav.latitud - originnav.latitud
            scale = 0.95
            ax.arrow(originnav.longitud, originnav.latitud, dx * scale, dy * scale, length_includes_head=True,
                      head_width=0.02, head_length=0.02, fc="purple", ec="purple",)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Mapa Espai Aeri -- Veïns de {origen}")
    ax.set_grid(True)

    return fig

def ShowShortestMap(airspace, origen, destino):
    nav_origen=None
    nav_destino=None

    for navpoint in airspace.list_navpoints:
        if navpoint.name==origen:
            nav_origen=navpoint
            break

    for navpoint in airspace.list_navpoints:
        if navpoint.name == destino:
            nav_destino = navpoint
            break
    if nav_origen==None or nav_destino==None:
        return None

def Reachability(airspace, navpoint):
    for navpoint in airspace.list_navpoints:
        if navpoint==NavPoint.name:
            origin=navpoint
            break
    i=0

    found=False
    while i<len(graph.nodes):
        if graph.nodes[i]==origin:
            found=True
        i=i+1
    i=i-1
    if found:
        reach=[origin]
        new=True
        while new:
            new=False
            for node in reach:
                for vecino in node.list_of_neighbours:
                    if vecino not in reach:
                        reach.append(vecino)
                        new=True
        print(reach[0].name)
        return reach

def FindShortestPath(graph, origin, destination):
    for nodes in graph.nodes:
        if nodes.name==origin:
            origin=nodes
        elif nodes.name==destination:
            destination=nodes

    camins_possibles=[]

    camino_inicial=Path()
    AddNodeToPath(camino_inicial, origin)
    camins_possibles.append(camino_inicial)

    found=False
    resultado=None

    while len(camins_possibles)!=0 and found==False:
        # Ordena caminos por coste estimado (puedes añadir atributo si quieres)
        camins_possibles.sort(key=lambda p: len(p.nodelist))

        camino_actual = camins_possibles.pop(0)  # saca el mejor camino
        nodo_actual = camino_actual.nodelist[-1]

        for vecino in nodo_actual.list_of_neighbours:
            # Evita ciclos
            if vecino in camino_actual.nodelist:
                continue

            nuevo_camino = camino_actual.copy()
            AddNodeToPath(nuevo_camino, vecino)

            if vecino == destination:
                found = True
                resultado = nuevo_camino
                break  # terminamos

            camins_possibles.append(nuevo_camino)

    if found:
        print("Camino encontrado:")
        for nodo in resultado.nodelist:
            print(nodo.name, end=" → ")
        print("FIN")
        return resultado
    else:
        print("No se encontró camino.")
        return None
