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

#li donem  mida i títol a la finestra i creem les files i columnes necessàries //estructura de la finestra
fin=tk.Tk()
fin.geometry("1000x600")
fin.title("Interfaç gràfica V1")
fin.columnconfigure(0, weight=1)
fin.columnconfigure(1, weight=10)
fin.rowconfigure(0, weight=1)
fin.rowconfigure(1, weight=1)
fin.rowconfigure(2, weight=1)
fin.rowconfigure(3, weight=1)


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

#Configuració espai pels inputs
inputframe=tk.LabelFrame(fin,text="Tria del node d'origen:")
inputframe.grid(row=3,column=0,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputframe.rowconfigure(0, weight=1)
inputframe.rowconfigure(1, weight=1)
inputframe.columnconfigure(0, weight=1)

entry=tk.Entry(inputframe)
entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputframe, text="Input", command=showtext)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai pels grafics/imatges
pictureframe=tk.LabelFrame(fin, text="Visualització dels grafos")
pictureframe.grid(row=0, column=1, rowspan=4, padx=5, pady=5, sticky="nsew")

pictureframe.rowconfigure(0, weight=1)
pictureframe.columnconfigure(0, weight=1)

fin.mainloop()