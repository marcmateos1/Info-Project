from graph import *
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import filedialog

selected_file="ElsMeusNodesSegments.txt"

def SelectedFile():
    global selected_file
    messagebox.showinfo("Treballant amb l'arxiu .txt: ", entry_file.get())
    text=entry_file.get()+".txt"
    selected_file=text

    if not os.path.exists(selected_file):
        with open(selected_file, "w") as f:
            pass  # crea el archivo vacío

def SaveFile():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             title="Desa com...")

    F=open(selected_file,"r")
    line=F.readline()
    contingut=""
    while line!="":
        contingut=contingut+line
        line=F.readline()

    F.close()

    if filepath:
        with open(filepath, "w") as f:
            f.write(contingut)
        print(f"Arxiu desat a: {filepath}")

    if selected_file!="ElsMeusNodesSegments.txt":
        fitxer_temporal = selected_file
        if os.path.exists(fitxer_temporal):
            os.remove(fitxer_temporal)

def CarregarFicher():
    global selected_file
    ruta_fitxer = filedialog.askopenfilename(
        title="Selecciona un fitxer .txt",
        filetypes=[("Fitxers de text", "*.txt")]
    )
    if ruta_fitxer:
        print("Has seleccionat:", ruta_fitxer)
        with open(ruta_fitxer, "r", encoding="utf-8") as fitxer:
            contingut = fitxer.read()
            print("Contingut del fitxer:")
            print(contingut)

        selected_file="document_nou.txt"
        with open(selected_file, "w") as f:
            f.writelines(contingut)

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
    A = CreateGraphFromFiles(selected_file)
    Plot(A)

def showgrafofromfiles_veins():
    A= CreateGraphFromFiles(selected_file)
    node_origin_for_grafos = entry.get()
    PlotNode(A, node_origin_for_grafos)

def AddNodeToTheFile():
    messagebox.showinfo("Text introduït: ", entry_node.get())
    newtext=entry_node.get()
    F=open(selected_file, "a")
    F.write("Node "+newtext+"\n")
    F.close()

def AddSegmentToTheFile():
    messagebox.showinfo("Text introduït: ", entry_segment.get())
    newtext=entry_segment.get()
    F=open(selected_file, "a")
    F.write("Segment "+newtext+"\n")
    F.close()

def DeleteNodeToTheFile():
    messagebox.showinfo("Text introduït: ", entry_node_delete.get())
    deletetext="Node "+entry_node_delete.get()
    deletetext_seccions=deletetext.rstrip().split()
    F=open(selected_file, "r")
    line=F.readline()
    lineswanted=[]
    while line!="":
        trozos=line.rstrip().split(" ")
        if trozos[0]=="Node":
            if trozos[1]!=deletetext_seccions[1]:
                lineswanted.append(line)
        elif trozos[0]=="Segment":
            if trozos[2]!=deletetext_seccions[1] and trozos[3]!=deletetext_seccions[1]:
                lineswanted.append(line)
        line=F.readline()
    F.close()
    L = open(selected_file, "w")
    L.writelines(lineswanted)
    L.close()

def DeleteSegmentToTheFile():
    messagebox.showinfo("Text introduït: ", entry_segment_delete.get())
    deletetext="Segment "+entry_segment_delete.get()
    deletetext_seccions=deletetext.rstrip().split()
    F=open(selected_file, "r")
    line=F.readline()
    lineswanted=[]
    while line!="":
        trozos=line.rstrip().split(" ")
        if trozos[2]!=deletetext_seccions[2] or trozos[3]!=deletetext_seccions[3]:
            lineswanted.append(line)
        line=F.readline()
    F.close()
    L = open(selected_file, "w")
    L.writelines(lineswanted)
    L.close()


#li donem  mida i títol a la finestra i creem les files i columnes necessàries //estructura de la finestra
fin=tk.Tk()
fin.geometry("1000x600")
fin.title("Interfaç gràfica V1")
fin.columnconfigure(0, weight=1)
fin.columnconfigure(1, weight=1)
fin.columnconfigure(2, weight=1)
fin.columnconfigure(3,weight=1)
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
inputnode=tk.LabelFrame(fin,text="Afegeix un node (name, cord x, cord y)")
inputnode.grid(row=1,column=1,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputnode.rowconfigure(0, weight=1)
inputnode.rowconfigure(1, weight=1)
inputnode.columnconfigure(0, weight=1)

entry_node=tk.Entry(inputnode)
entry_node.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputnode, text="Input", command=AddNodeToTheFile)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai pels inputs Add Segment
inputsegment=tk.LabelFrame(fin,text="Afegeix un segment (name, origin, dest)")
inputsegment.grid(row=2,column=1,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputsegment.rowconfigure(0, weight=1)
inputsegment.rowconfigure(1, weight=1)
inputsegment.columnconfigure(0, weight=1)

entry_segment=tk.Entry(inputsegment)
entry_segment.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputsegment, text="Input", command=AddSegmentToTheFile)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració delete nodes
inputdeletenode=tk.LabelFrame(fin,text="Elimina un node (name)")
inputdeletenode.grid(row=0,column=2,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputdeletenode.rowconfigure(0, weight=1)
inputdeletenode.rowconfigure(1, weight=1)
inputdeletenode.columnconfigure(0, weight=1)

entry_node_delete=tk.Entry(inputdeletenode)
entry_node_delete.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputdeletenode, text="Input", command=DeleteNodeToTheFile)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració delete segments
inputdeletesegment=tk.LabelFrame(fin,text="Elimina un segment (name, origin, dest)")
inputdeletesegment.grid(row=1,column=2,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inputdeletesegment.rowconfigure(0, weight=1)
inputdeletesegment.rowconfigure(1, weight=1)
inputdeletesegment.columnconfigure(0, weight=1)

entry_segment_delete=tk.Entry(inputdeletesegment)
entry_segment_delete.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inputdeletesegment, text="Input", command=DeleteSegmentToTheFile)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#Configuració espai guardar el file
guardat=tk.LabelFrame(fin,text="Selecciona fitxer")
guardat.grid(row=2,column=2,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

guardat.rowconfigure(0, weight=1)
guardat.rowconfigure(1, weight=1)
guardat.rowconfigure(2, weight=1)
guardat.rowconfigure(3, weight=1)
guardat.columnconfigure(0, weight=1)

entry_file=tk.Entry(guardat)
entry_file.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(guardat, text="Input", command=SelectedFile)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(guardat, text="Guardar arxiu seleccionat", command=SaveFile)
button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button_charge=tk.Button(guardat, text="Input", command=SelectedFile)
button_charge.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button_charge=tk.Button(guardat, text="Carregar fichero", command=CarregarFicher)
button_charge.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#configuracio triar node per reachability
reach=tk.LabelFrame(fin,text="Tria node(Reachability)")
reach.grid(row=0,column=3,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

reach.rowconfigure(0, weight=1)
reach.rowconfigure(1, weight=1)
reach.columnconfigure(0, weight=1)

entry=tk.Entry(reach)
entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(reach, text="Input", command=showtext)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)


#configuracio node inici spath
inici=tk.LabelFrame(fin,text="Tria node d'inici (Shortest path)")
inici.grid(row=1,column=3,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

inici.rowconfigure(0, weight=1)
inici.rowconfigure(1, weight=1)
inici.columnconfigure(0, weight=1)

entry=tk.Entry(inici)
entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(inici, text="Input", command=showtext)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

#configuracio node final spath
final=tk.LabelFrame(fin,text="Tria node final (Shortest path)")
final.grid(row=2,column=3,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

final.rowconfigure(0, weight=1)
final.rowconfigure(1, weight=1)
final.columnconfigure(0, weight=1)

entry=tk.Entry(final)
entry.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)

button=tk.Button(final, text="Input", command=showtext)
button.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N + tk.E + tk.W + tk.S)
fin.mainloop()