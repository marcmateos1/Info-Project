from segment import *
from path import Path, AddNodeToPath, ContainsNode, PlotPath
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        """Inicializa un grafo con listas vacías de nodos y segmentos."""
        self.nodes = []
        self.segments = []

def get_node_by_name(graph, name):
    i=0
    for elements in graph.nodes:
        if graph.nodes[i].name==name:
            return graph.nodes[i]
        i=i+1
    return None

def AddNode(g, n):
    if n in g.nodes:
        return False
    g.nodes.append(n)
    return True

def AddSegment(g, name, nameOrigin, nameDestination):

    origin = next((node for node in g.nodes if node.name == nameOrigin), None)
    destination = next((node for node in g.nodes if node.name == nameDestination), None)

    if origin is None or destination is None:
        return False  # Uno o ambos nodos no existen

    segment = Segment(name, origin, destination)
    g.segments.append(segment)
    AddNeighbour(origin, destination)  # Agregar destino a la lista de vecinos de origen
    return True

def AddSegmentFile (g ,name, nodeOrigin, nodeDestination):
    segment = Segment(name, nodeOrigin, nodeDestination)
    g.segments.append(segment)
    AddNeighbour(nodeOrigin, nodeDestination)  # Agregar destino a la lista de vecinos de origen
    return True


def GetClosest(g, x, y):
    """Devuelve el nodo más cercano a la posición (x, y)."""
    return min(g.nodes, key=lambda n: Distance(n, Node("temp", x, y)))


def Plot(g):
    """Dibuja el grafo con sus nodos y segmentos, mostrando los costos en los segmentos."""
    #plt.figure(figsize=(10, 7))

    for segment in g.segments:   #es un bucle for on segment es una variable que fa referencia a cadascun dels valors de la llista g.segments
        x_values = [segment.originnode.x, segment.destnode.x]
        y_values = [segment.originnode.y, segment.destnode.y]
        plt.plot(x_values, y_values, 'grey', linewidth=1)  # Dibujar el segmento

        # Mostrar el costo en el centro del segmento
        mid_x = (segment.originnode.x + segment.destnode.x) / 2
        mid_y = (segment.originnode.y + segment.destnode.y) / 2
        plt.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color="red")  #la f del principi es de f-string on es pot ficaar text i variables
                                                                                    # el .2f significa que se especifiquen dos decimals en format float de f
    for node in g.nodes:
        plt.scatter(node.x, node.y, color='blue', s=100)
        plt.text(node.x, node.y, node.name, fontsize=12, color="black")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Graph Representation")
    plt.grid()
    plt.show()

def PlotNode(g, nameOrigin):
    """Dibuja el grafo resaltando el nodo de origen y sus vecinos."""
    node_origin = next((node for node in g.nodes if node.name == nameOrigin), None)
    if node_origin is None:
        return False  # El nodo no existe

    #plt.figure(figsize=(10, 7)) dimensionar grafic

    for segment in g.segments:
        x_values = [segment.originnode.x, segment.destnode.x]
        y_values = [segment.originnode.y, segment.destnode.y]
        color = 'grey'
        if segment.originnode == node_origin and segment.destnode in node_origin.list_of_neighbours:
            color = 'red'  # Resaltar segmentos conectados al nodo origen
            dx=segment.destnode.x-segment.originnode.x
            dy=segment.destnode.y-segment.originnode.y
            plt.arrow(segment.originnode.x,segment.originnode.y, dx ,dy, head_width=0.5, head_length=1, length_includes_head=True)

        plt.plot(x_values, y_values, color=color, linewidth=1)

        # Mostrar el costo del segmento
        mid_x = (segment.originnode.x + segment.destnode.x) / 2
        mid_y = (segment.originnode.y + segment.destnode.y) / 2
        plt.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color="red")

    for node in g.nodes:
        color = 'gray'
        if node == node_origin:
            color = 'blue'  # Nodo origen en azul
        elif node in node_origin.list_of_neighbours:
            color = 'green'  # Vecinos en verde
        plt.scatter(node.x, node.y, color=color, s=100)
        plt.text(node.x, node.y, node.name, fontsize=12, ha='right', color="black")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Graph with Node {nameOrigin} Highlighted")
    plt.grid()
    plt.show()

    return True

def PlotForPath(g, ax):
    for segment in g.segments:   #es un bucle for on segment es una variable que fa referencia a cadascun dels valors de la llista g.segments
        x_values = [segment.originnode.x, segment.destnode.x]
        y_values = [segment.originnode.y, segment.destnode.y]
        plt.plot(x_values, y_values, 'grey', linewidth=1)  # Dibujar el segmento

        # Mostrar el costo en el centro del segmento
        mid_x = (segment.originnode.x + segment.destnode.x) / 2
        mid_y = (segment.originnode.y + segment.destnode.y) / 2
        plt.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color="grey")  #la f del principi es de f-string on es pot ficaar text i variables
                                                                                    # el .2f significa que se especifiquen dos decimals en format float de f
    for node in g.nodes:
        plt.scatter(node.x, node.y, color='grey', s=100)
        plt.text(node.x, node.y, node.name, fontsize=12, color="black")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)


def CreateGraphFromFiles(file):
    M = Graph()
    F = open(file, "r")  # llegir arxiu
    nodelist=[] #llista per guardar els nodes
    lineas = F.readline()
    while lineas!="": #llegir arxiu fins ultima fila
        trozos=lineas.rstrip().split()

        if trozos[0]=="Node":
            n=Node(trozos[1], float(trozos[2]),float(trozos[3]))
            nodelist.append(n)
            AddNode(M , n)


        if trozos[0]=="Segment":
            for valores in nodelist:
                i=0
                foundorigen=False
                founddestino=False

                while i<len(nodelist):
                    if trozos[2]==nodelist[i].name:
                        origen=nodelist[i]
                        foundorigen=True
                    if trozos[3]==nodelist[i].name:
                        destino=nodelist[i]
                        founddestino=True
                    i=i+1

                if foundorigen==True and founddestino==True:
                    AddSegmentFile(M, trozos[1], origen, destino)

        lineas = F.readline()

    F.close()
    return M

def CreateGraph_1():
    G = Graph()
    AddNode(G, Node("A", 1, 20))
    AddNode(G, Node("B", 8, 17))
    AddNode(G, Node("C", 15, 20))
    AddNode(G, Node("D", 18, 15))
    AddNode(G, Node("E", 2, 4))
    AddNode(G, Node("F", 6, 5))
    AddNode(G, Node("G", 12, 12))
    AddNode(G, Node("H", 10, 3))
    AddNode(G, Node("I", 19, 1))
    AddNode(G, Node("J", 13, 5))
    AddNode(G, Node("K", 3, 15))
    AddNode(G, Node("L", 4, 10))

    AddSegment(G, "AB", "A", "B")
    AddSegment(G, "AE", "A", "E")
    AddSegment(G, "AK", "A", "K")
    AddSegment(G, "BA", "B", "A")
    AddSegment(G, "BC", "B", "C")
    AddSegment(G, "BF", "B", "F")
    AddSegment(G, "BK", "B", "K")
    AddSegment(G, "BG", "B", "G")
    AddSegment(G, "CD", "C", "D")
    AddSegment(G, "CG", "C", "G")
    AddSegment(G, "DG", "D", "G")
    AddSegment(G, "DH", "D", "H")
    AddSegment(G, "DI", "D", "I")
    AddSegment(G, "EF", "E", "F")
    AddSegment(G, "FL", "F", "L")
    AddSegment(G, "GB", "G", "B")
    AddSegment(G, "GF", "G", "F")
    AddSegment(G, "GH", "G", "H")
    AddSegment(G, "ID", "I", "D")
    AddSegment(G, "IJ", "I", "J")
    AddSegment(G, "JI", "J", "I")
    AddSegment(G, "KA", "K", "A")
    AddSegment(G, "KL", "K", "L")
    AddSegment(G, "LK", "L", "K")
    AddSegment(G, "LF", "L", "F")

    return G


def Reachability(graph, nodename):
    for node in graph.nodes:
        if nodename==node.name:
            origin=node
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



def Plot_All_Paths(graph, reachable_nodes):
    fig, ax = plt.subplots()
    PlotForPath(graph, ax)
    origin=reachable_nodes[0]
    def AddPossiblePaths(graph, reachable_nodes):
        i = 1
        all_paths = []
        while i < len(reachable_nodes):
            n = FindShortestPath(graph, reachable_nodes[0], reachable_nodes[i])
            all_paths.append(n)
            i = i + 1
        return all_paths

    all_paths=AddPossiblePaths(graph, reachable_nodes)

    PlotForPath(graph,ax)
    for nodes in reachable_nodes:
        plt.scatter(nodes.x,nodes.y, color="blue", s=100)
    for path in all_paths:
        for i in range(len(path.nodelist)-1):
            n1 = path.nodelist[i]
            n2 = path.nodelist[i + 1]
            ax.plot([n1.x, n2.x], [n1.y, n2.y], color="green", linewidth=2)

            for segment in graph.segments:
                if segment.originnode.name == n1.name and segment.destnode.name == n2.name:
                    mid_x = (segment.originnode.x + segment.destnode.x) / 2
                    mid_y = (segment.originnode.y + segment.destnode.y) / 2
                    plt.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color="blue")

                    dx = segment.destnode.x - segment.originnode.x
                    dy = segment.destnode.y - segment.originnode.y
                    plt.arrow(segment.originnode.x, segment.originnode.y, dx, dy, head_width=0.5, head_length=1,
                              length_includes_head=True, color="green")
    plt.scatter(origin.x, origin.y, color="red", s=100)
    plt.title("Reachability map")
    plt.show()


def FindShortestPath(graph, origin, destination):
    for nodes in graph.nodes:
        if nodes.name==origin.name:
            origin=nodes
        elif nodes.name==destination.name:
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