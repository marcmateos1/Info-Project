import matplotlib.pyplot as plt


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
    else:
        return False

def CostToNode(path, node):
    if node in path.nodelist:
        i=0
        while i<(len(path.nodelist)-1)
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

