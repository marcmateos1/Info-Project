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
        self.nav_list=[]

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
    airspace.nav_list=[]
    fig=Figure()
    ax=fig.add_subplot(111)
    for navpoint in airspace.list_navpoints:
        ax.scatter(navpoint.longitud, navpoint.latitud, color="blue", s=10)
        ax.text(navpoint.longitud, navpoint.latitud, navpoint.name, fontsize=6, color="black")
        airspace.nav_list.append(navpoint)
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
    nav_list=[]
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

    nav_list.append(nav_buscat)

    for segment in airspace.list_navsegments:

        found_origin=False
        found_dest=False


        for navpoints in airspace.list_navpoints:
            if navpoints.number==segment.originnumber:
                originnav=navpoints
                found_origin=True
                nav_list.append(originnav)

            elif navpoints.number==segment.destnumber:
                destnav=navpoints
                found_dest=True
                nav_list.append(destnav)
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
    a=False
    b=False
    for airport in airspace.list_navairports:
        if airport.name == origen:
            originname = airport.sids[0]
            for navpoint in airspace.list_navpoints:
                if navpoint.name==originname:
                    nav_origen=navpoint
                    a=True
        if airport.name == destino:
            destname=airport.stars[0]
            for navpoint in airspace.list_navpoints:
                if navpoint.name==destname:
                    nav_destino = navpoint
                    b=True
        if a==True and b==True:
            break

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


def ReachabilityFromAirport(airspace, airport_name):
    # Buscar el aeropuerto
    airport = None
    for a in airspace.list_navairports:
        if a.name.strip() == airport_name.strip():
            airport = a
            break
    if airport is None:
        print(f"Aeropuerto '{airport_name}' no encontrado.")
        return []

    # Buscar NavPoints asociados a sus SIDs
    starting_navpoints = []
    for sid_name in airport.sids:
        for nav in airspace.list_navpoints:
            if nav.name == sid_name.strip():
                starting_navpoints.append(nav)
                break

    if not starting_navpoints:
        print(f"No se encontraron NavPoints para los SIDs de {airport_name}.")
        return []

    # Visitar todos los alcanzables desde cada SID
    visited = set()
    to_visit = starting_navpoints.copy()

    while to_visit:
        current = to_visit.pop()
        if current.number in visited:
            continue
        visited.add(current.number)

        # Añadir vecinos conectados desde segmentos
        for seg in airspace.list_navsegments:
            if seg.originnumber == current.number:
                # Buscar el NavPoint destino
                for nav in airspace.list_navpoints:
                    if nav.number == seg.destnumber and nav.number not in visited:
                        to_visit.append(nav)
                        break

    # Devolver lista de NavPoints alcanzables
    return [nav for nav in airspace.list_navpoints if nav.number in visited]

def PlotReachabilityFromAirport(airspace, airport_name):
    fig=Figure()
    ax=fig.add_subplot(111)
    reachable_navpoints = ReachabilityFromAirport(airspace, airport_name)
    reachable_ids = set(nav.number for nav in reachable_navpoints)

    # Dibuja los navpoints
    for nav in reachable_navpoints:
        ax.scatter(nav.longitud, nav.latitud, color="blue", s=10)
        ax.text(nav.longitud, nav.latitud, nav.name, fontsize=6, color="black")

    # Dibuja los segmentos con flechas
    for segment in airspace.list_navsegments:
        if segment.originnumber in reachable_ids and segment.destnumber in reachable_ids:
            origin_nav = next(n for n in reachable_navpoints if n.number == segment.originnumber)
            dest_nav = next(n for n in reachable_navpoints if n.number == segment.destnumber)

            dx = dest_nav.longitud - origin_nav.longitud
            dy = dest_nav.latitud - origin_nav.latitud

            ax.arrow(origin_nav.longitud, origin_nav.latitud,
                      dx, dy,
                      head_width=0.02, head_length=0.02,
                      fc='purple', ec='purple', length_includes_head=True)

    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.set_title(f"Reachability desde l'aeroport {airport_name}")
    ax.grid(True)

    return fig

def kml_point(name, navpoint): #funcio per escriure cada navpoint en format kml
    description=navpoint.name
    longitude=navpoint.longitud
    latitude=navpoint.latitud
    return f"""
    <Placemark>
      <name>{name}</name>
      <description>{description}</description>
      <Point>
        <coordinates>{longitude},{latitude}</coordinates>
      </Point>
    </Placemark>
    """

def kml_line(name, coords):
    """
    coords: list of (longitude, latitude)
    """
    coord_text = "\n".join([f"{lon},{lat}" for lon, lat in coords])
    return f"""
    <Placemark>
      <name>{name}</name>
      <LineString>
        <coordinates>
          {coord_text}
        </coordinates>
      </LineString>
    </Placemark>
    """

def convertir_txt_a_kml(archivo_txt, archivo_kml):
    # Leer el contenido del archivo .txt
    with open(archivo_txt, 'r', encoding='utf-8') as f:
        placemarks = f.read()

    # Crear estructura KML completa
    kml_completo = f'''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
{placemarks}
  </Document>
</kml>'''

    # Guardar en nuevo archivo .kml
    with open(archivo_kml, 'w', encoding='utf-8') as f:
        f.write(kml_completo)

    print(f"Archivo KML creado: {archivo_kml}")

