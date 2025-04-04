import matplotlib.pyplot as plt
from segment import *


class Graph:
    def __init__(self):
        """Inicializa un grafo con listas vacías de nodos y segmentos."""
        self.nodes = []
        self.segments = []


def AddNode(g, n):
    if n in g.nodes:
        return False
    g.nodes.append(n)
    return True


def AddSegment(g, name, nameOrigin, nameDestination):
    """Agrega un segmento al grafo entre dos nodos existentes.
    También actualiza la lista de vecinos del nodo origen."""
    origin = next((node for node in g.nodes if node.name == nameOrigin), None)
    destination = next((node for node in g.nodes if node.name == nameDestination), None)

    if origin is None or destination is None:
        return False  # Uno o ambos nodos no existen

    segment = Segment(name, origin, destination)
    g.segments.append(segment)
    AddNeighbour(origin, destination)  # Agregar destino a la lista de vecinos de origen
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
            plt.arrow(segment.originnode.x,segment.originnode.y, dx ,dy, head_width=0.5, head_length=1)

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


def CreateGraphFromFiles(file):
    M = Graph()
    F = open(file, "r")  # llegir arxiu
    nodelist=[]
    lineas = F.readline()
    while lineas!="":
        trozos=lineas.rstrip().split()
        if trozos[0]=="Node":
            n=Node(trozos[1], float(trozos[2]),float(trozos[3]))
            nodelist.append(n)
            AddNode(M , n)
            print(nodelist)

        if trozos[0]=="Segment":
            for valores in nodelist:
                i=0
                while i<len(nodelist):
                    if trozos[2]==nodelist[i].name:
                        origen=nodelist[i]
                    if trozos[3]==nodelist[i].name:
                        destino=nodelist[i]
                    i=i+1

            AddSegment(M, trozos[1], origen, destino)

        lineas = F.readline()

    F.close()
    return M

