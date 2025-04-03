import matplotlib.pyplot as plt
from segment import *


class Graph:
    def __init__(self):
        """Inicializa un grafo con listas vacías de nodos y segmentos."""
        self.nodes = []
        self.segments = []


def AddNode(g, n):
    """Agrega un nodo al grafo. Devuelve False si ya existe y True si se añade."""
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
    plt.figure(figsize=(10, 7))

    for segment in g.segments:
        x_values = [segment.origin.x, segment.destination.x]
        y_values = [segment.origin.y, segment.destination.y]
        plt.plot(x_values, y_values, 'k-', linewidth=1)  # Dibujar el segmento

        # Mostrar el costo en el centro del segmento
        mid_x = (segment.origin.x + segment.destination.x) / 2
        mid_y = (segment.origin.y + segment.destination.y) / 2
        plt.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color="red")

    for node in g.nodes:
        plt.scatter(node.x, node.y, color='blue', s=100)
        plt.text(node.x, node.y, node.name, fontsize=12, ha='right', color="black")

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

    plt.figure(figsize=(10, 7))

    for segment in g.segments:
        x_values = [segment.originnode.x, segment.destnode.x]
        y_values = [segment.originnode.y, segment.destnode.y]
        color = 'blue'
        if segment.originnode == node_origin and segment.destnode in node_origin.list_of_neighbours:
            color = 'red'  # Resaltar segmentos conectados al nodo origen
        plt.plot(x_values, y_values, color=color, linewidth=1)

        # Mostrar el costo del segmento
        mid_x = (segment.originnode.x + segment.destnode.x) / 2
        mid_y = (segment.originnode.y + segment.destnode.y) / 2
        plt.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color="red")

    for node in g.nodes:
        color = 'red'
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