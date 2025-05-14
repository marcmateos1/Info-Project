from navAirpoint import NavAirport
from navPoint import NavPoint
from navSegment import NavSegment
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from path import Path, AddNavDistToMap

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
    ax.grid(True)

    return fig

def FindShortestMap(airspace, origen, destino):

    nav_origen = None
    nav_destino = None

    for navpoint in airspace.list_navpoints:
        if navpoint.name == origen:
            nav_origen = navpoint
            print("hola")
        if navpoint.name == destino:
            nav_destino = navpoint
            print("adios")

    if nav_origen is None or nav_destino is None:
        print("Origen o destino no encontrado.")
        return None

    camins_possibles = []

    camino_inicial = Path()
    AddNavDistToMap(camino_inicial, nav_origen, 0)  # Inicia con 0 distancia
    camins_possibles.append(camino_inicial)

    visited = set()
    resultado = None

    while camins_possibles:
        camins_possibles.sort(key=lambda p: p.total_distance)
        camino_actual = camins_possibles.pop(0)
        nodo_actual = camino_actual.nodelist[-1]

        if nodo_actual == nav_destino:
            resultado = camino_actual
            break

        if nodo_actual.number in visited:
            continue
        visited.add(nodo_actual.number)

        for segment in airspace.list_navsegments:
            if segment.originnumber == nodo_actual.number:
                vecino = next((p for p in airspace.list_navpoints if p.number == segment.destnumber), None)
                if vecino is None or vecino in camino_actual.nodelist:
                    continue

                nuevo_camino = camino_actual.copy()
                AddNavDistToMap(nuevo_camino, vecino, float(segment.distance))  # Agrega distancia real
                camins_possibles.append(nuevo_camino)

    if resultado:
        print("Camino más corto por distancia:")
        for nodo in resultado.nodelist:
            print(nodo.name, end=" → ")
        print("FIN\nDistancia total:", resultado.total_distance)
        return resultado
    else:
        print("No se encontró camino.")
        return None

def PlotShortestPath(airspace, path):
    fig=Figure()
    ax=fig.add_subplot(111)
    # Dibuja todos los navpoints
    for navpoint in airspace.list_navpoints:
        ax.scatter(navpoint.longitud, navpoint.latitud, color="lightgray", s=10)
        ax.text(navpoint.longitud, navpoint.latitud, navpoint.name, fontsize=6, color="gray")

    # Dibuja todos los segmentos en gris claro
    for segment in airspace.list_navsegments:
        origin = next((p for p in airspace.list_navpoints if p.number == segment.originnumber), None)
        dest = next((p for p in airspace.list_navpoints if p.number == segment.destnumber), None)
        if origin and dest:
            ax.plot([origin.longitud, dest.longitud], [origin.latitud, dest.latitud], color="lightgray", linewidth=0.5)

    # Ahora dibuja el camino más corto
    for i in range(len(path.nodelist) - 1):
        origen = path.nodelist[i]
        destino = path.nodelist[i + 1]

        dx = destino.longitud - origen.longitud
        dy = destino.latitud - origen.latitud

        ax.arrow(
            origen.longitud, origen.latitud, dx, dy,
            head_width=0.05, head_length=0.05, fc="red", ec="red", length_includes_head=True
        )

    # Marcar origen y destino
    ax.scatter(path.nodelist[0].longitud, path.nodelist[0].latitud, color="green", s=30, label="Origen")
    ax.scatter(path.nodelist[-1].longitud, path.nodelist[-1].latitud, color="red", s=30, label="Destino")

    ax.set_title(f"Shortest path between {path.nodelist[0].name} and {path.nodelist[-1].name}")
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.legend()
    ax.grid(True)

    return fig