from graph import *
import tkinter as tk
from tkinter import messagebox

#node_origin_for_grafos="A"

def showtext():
    messagebox.showinfo("Text introduït: ", entry.get())
    node_origin_for_grafos=entry.get()
    print(node_origin_for_grafos)

def showgrafoexemple():
    A = CreateGraph_1()
    Plot(A)

def showgrafoexemple_vaeïns():
    A = CreateGraph_1()
    node_origin_for_grafos=entry.get()
    PlotNode(A, node_origin_for_grafos)

def showgrafoinventat():
    A = CreateGraph_2()
    Plot(A)

def showgrafoinventat_vaeïns():
    A = CreateGraph_2()
    node_origin_for_grafos=entry.get()
    PlotNode(A, node_origin_for_grafos)

def showgrafofromfiles():
    A = CreateGraphFromFiles("ElsMeusNodesSegments.txt")
    Plot(A)

def showgrafofromfiles_veins():
    A= CreateGraphFromFiles("ElsMeusNodesSegments.txt")
    node_origin_for_grafos = entry.get()
    PlotNode(A, node_origin_for_grafos)

def AddNodeToTheFile():
    messagebox.showinfo("Text introduït: ", entry_node.get())
    newtext=entry_node.get()
    F=open("ElsMeusNodesSegments.txt", "a")
    F.write(newtext+"\n")
    F.close()

def AddSegmentToTheFile():
    messagebox.showinfo("Text introduït: ", entry_segment.get())
    newtext=entry_segment.get()
    F=open("ElsMeusNodesSegments.txt", "a")
    F.write(newtext+"\n")
    F.close()


#li donem  mida i títol a la finestra i creem les files i columnes necessàries //estructura de la finestra
fin=tk.Tk()
fin.geometry("1000x600")
fin.title("Interfaç gràfica V1")
fin.columnconfigure(0, weight=1)
fin.columnconfigure(1, weight=1)
fin.columnconfigure(2, weight=1)
fin.rowconfigure(0, weight=1)
fin.rowconfigure(1, weight=1)
fin.rowconfigure(2, weight=1)


#Configuració espai grafics exemple
graficsexemple=tk.LabelFrame(fin,text="Grafo de exemple:")
graficsexemple.grid(row=0,column=0,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

graficsexemple.rowconfigure(0, weight=1)
graficsexemple.rowconfigure(1, weight=1)
graficsexemple.columnconfigure(0, weight=1)

button1=tk.Button(graficsexemple, text="Mapa grafo", command=showgrafoexemple)
button1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button2=tk.Button(graficsexemple, text="Grafo amb veïns", command=showgrafoexemple_vaeïns)
button2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai grafics inventat
graficinventat=tk.LabelFrame(fin,text="El nostre grafo inventat:")
graficinventat.grid(row=1,column=0,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

graficinventat.rowconfigure(0, weight=1)
graficinventat.rowconfigure(1, weight=1)
graficinventat.columnconfigure(0, weight=1)

button1=tk.Button(graficinventat, text="Mapa grafo", command=showgrafoinventat)
button1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button2=tk.Button(graficinventat, text="Grafo amb veïns", command=showgrafoinventat_vaeïns)
button2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai grafics del arxiu text
grafictext=tk.LabelFrame(fin,text="Grafo llegint un document:")
grafictext.grid(row=2,column=0,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

grafictext.rowconfigure(0, weight=1)
grafictext.rowconfigure(1, weight=1)
grafictext.columnconfigure(0, weight=1)

button1=tk.Button(grafictext, text="Mapa grafo", command=showgrafofromfiles)
button1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button2=tk.Button(grafictext, text="Grafo amb veïns", command=showgrafofromfiles_veins)
button2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#button3=tk.Button(espaigrafics, text="Grafic arxiu")
#button3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai pels input buscar node
inputframe=tk.LabelFrame(fin,text="Tria del node d'origen:")
inputframe.grid(row=0,column=1,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputframe.rowconfigure(0, weight=1)
inputframe.rowconfigure(1, weight=1)
inputframe.columnconfigure(0, weight=1)

entry=tk.Entry(inputframe)
entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputframe, text="Input", command=showtext)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai pels inputs Add Node
inputnode=tk.LabelFrame(fin,text="Afegeix un node (-Node-, name, cord x, cord y)")
inputnode.grid(row=1,column=1,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputnode.rowconfigure(0, weight=1)
inputnode.rowconfigure(1, weight=1)
inputnode.columnconfigure(0, weight=1)

entry_node=tk.Entry(inputnode)
entry_node.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputnode, text="Input", command=AddNodeToTheFile)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai pels inputs Add Segment
inputsegment=tk.LabelFrame(fin,text="Afegeix un segment (-Segment-, name, origin, dest)")
inputsegment.grid(row=2,column=1,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputsegment.rowconfigure(0, weight=1)
inputsegment.rowconfigure(1, weight=1)
inputsegment.columnconfigure(0, weight=1)

entry_segment=tk.Entry(inputsegment)
entry_segment.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputsegment, text="Input", command=AddSegmentToTheFile)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració delete nodes
inputdeletenode=tk.LabelFrame(fin,text="Elimina un node (-Node-, name, cord x, cord y)")
inputdeletenode.grid(row=0,column=2,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputdeletenode.rowconfigure(0, weight=1)
inputdeletenode.rowconfigure(1, weight=1)
inputdeletenode.columnconfigure(0, weight=1)

entry_node_delete=tk.Entry(inputdeletenode)
entry_node_delete.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputdeletenode, text="Input", command=showtext)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració delete segments
inputdeletesegment=tk.LabelFrame(fin,text="Elimina un segment (-Segment-, name, cord x, cord y)")
inputdeletesegment.grid(row=1,column=2,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputdeletesegment.rowconfigure(0, weight=1)
inputdeletesegment.rowconfigure(1, weight=1)
inputdeletesegment.columnconfigure(0, weight=1)

entry_segment_delete=tk.Entry(inputdeletesegment)
entry_segment_delete.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputdeletesegment, text="Input", command=showtext)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai guardar el file
guardat=tk.LabelFrame(fin,text="Guarda els canvis")
guardat.grid(row=2,column=2,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

fin.mainloop()