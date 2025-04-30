from node import *

class Segment:
    def __init__(self, name, originnode,destnode):
        self.name=name
        self.originnode=originnode
        self.destnode=destnode
        self.cost=Distance(originnode, destnode)

    def __str__(self):
        "Devuelve una representación en cadena del segmento."
        return f"Segmento {self.name}: {self.originnode.name} -> {self.destnode.name}, Cost: {self.cost:.2f}"


