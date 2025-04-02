class Node:
    def __init__(self, name,x, y):
        self.name=name
        self.x=float(x)
        self.y=float(y)
        self.list_of_neighbours=[]

def AddNeighbour(n1,n2):
    if n2 in n1.list_of_neighbours:
        print("El node no ha sigut agregat")
        return False
    n1.list_of_neighbours.append(n2)
    print("El node ha sigut agregat")
    return True
def Distance(n1,n2):
    distance=((n1.x-n2.x)**2+(n1.y-n2.y)**2)**(1/2)
    return distance
