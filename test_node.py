from node import *

n1=Node("aaa", 0, 0)
n2=Node("bbb",3,4)

#mostrar distancia
print(Distance(n1,n2))

#mostrar quan afegeixes nodes i quan no pots
print(AddNeighbour(n1,n2))
print(AddNeighbour(n1,n2))

print(n1.__dict__) #muestra atributos de n1

for n in n1.list_of_neighbours: #mostra atributs veïns
    print(n.__dict__)