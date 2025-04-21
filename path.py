import matplotlib.pyplot as plt
from graph import *
class Path:
    def __init__(self):
        self.nodelist=[]
        self.totalcost=0

def AddNodeToPath(path, node):
    if node not in path.nodelist:
        path.nodelist.append(node)


def ContainsNode(path, node):
    if node in path.nodelist:
        return True
    return False

def CostToNode(path, node):
    if node in path.nodelist:
        i=0
        while i<(len(path.nodelist)-1):
            d=Distance(path.nodelist[i], path.nodelist[i+1])
            path.totalcost=path.totalcost+d
            i=i+1
        df=Distance(node, path.nodelist[-1])
        path.totalcost=df+path.totalcost
        return path.totalcost
    else:
        a=-1
        return a
def PlotPath(graph, path):
    i=0
    for nodes in graph.nodes:
        if graph.nodes[i].name in path.nomsNodes:
            plt.scatter(graph.nodes[i].x,graph.nodes[i].y, color="red")
        else:
            plt.scatter(graph.nodes[i].x, graph.nodes[i].y, color="grey")
        plt.text(graph.nodes[i].x, graph.nodes[i].y, graph.nodes[i].name, fontsize=12, ha='right', color="black")
        i=i+1
    i=0
    for elements in graph.segments:    #es un bucle for on segment es una variable que fa referencia a cadascun dels valors de la llista g.segments

        if graph.segments[i].originnode in path.nodelist and graph.segments[i].destnode.name in path.nodelist:
            plt.plot([graph.segments[i].originnode.x,graph.segments[i].destnode.x ],[graph.segments[i].originnode.y,graph.segments[i].destnode.y ], color="blue")

            mid_x = (graph.segments[i].originnode.x + graph.segments[i].destnode.x) / 2
            mid_y = (graph.segments[i].originnode.y + graph.segments[i].destnode.y) / 2
            plt.text(mid_x, mid_y, f"{graph.segments[i].cost:.2f}", fontsize=10, color="red")

            dx = graph.segments[i].destnode.x - graph.segments[i].originnode.x
            dy = graph.segments[i].destnode.y - graph.segments[i].originnode.y
            plt.arrow(graph.segments[i].originnode.x, graph.segments[i].originnode.y, dx, dy, head_width=0.5, head_length=1,length_includes_head=True)
        else:
            plt.plot([graph.segments[i].originnode.x, graph.segments[i].destnode.x], [graph.segments[i].originnode.y, graph.segments[i].destnode.y], color="grey")
        i=i+1
    plt.grid()
    plt.show()

def ReachableNodes(graph, start_node_name):
    start_node = get_node_by_name(graph, start_node_name)
    return start_node.list_of_neighbours