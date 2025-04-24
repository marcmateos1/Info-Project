from graph_utils import*
from node import Distance

class Path:
    def __init__(self):
        self.nodelist=[]
        self.totalcost=0

    def copy(self):
        new_path = Path()
        new_path.nodelist = self.nodelist.copy()  # copia la lista de nodos
        return new_path

def AddNodeToPath(path, node):
    if node not in path.nodelist:
        path.nodelist.append(node)


def ContainsNode(path, node):
    if node in path.nodelist:
        return True
    return False

def CostToNode(path, node):
    for nodes in path.nodelist:
        if nodes.name==node:
            node=nodes
            i = 0
            while i < (len(path.nodelist) - 1):
                d = Distance(path.nodelist[i], path.nodelist[i + 1])
                path.totalcost = path.totalcost + d
                i = i + 1
            df = Distance(node, path.nodelist[-1])
            path.totalcost = df + path.totalcost
            return path.totalcost
    else:
        a=-1
        return a

def PlotPath(graph, path):
    fig, ax=plt.subplots()
    PlotForPath(graph, ax)
    for i in range(len(path.nodelist)-1):
        n1=path.nodelist[i]
        n2=path.nodelist[i+1]
        ax.plot([n1.x, n2.x], [n1.y, n2.y], color="green", linewidth=2)
        plt.scatter([n1.x,n2.x],[n1.y, n2.y], color="blue", s=100)

        for segment in graph.segments:
            if segment.originnode.name==n1.name and segment.destnode.name==n2.name:
                mid_x = (segment.originnode.x + segment.destnode.x) / 2
                mid_y = (segment.originnode.y + segment.destnode.y) / 2
                plt.text(mid_x, mid_y, f"{segment.cost:.2f}", fontsize=10, color="blue")

                dx = segment.destnode.x - segment.originnode.x
                dy = segment.destnode.y - segment.originnode.y
                plt.arrow(segment.originnode.x, segment.originnode.y, dx, dy, head_width=0.5, head_length=1,length_includes_head=True, color="green")
    ax.set_title("Camí seleccionat")
    plt.show()

