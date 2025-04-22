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
