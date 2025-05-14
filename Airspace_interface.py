import tkinter as tk
from tkinter import messagebox
import os
from tkinter import filedialog
from airSpace import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#g=AirSpace()
#LoadNavPoints("cat_nav", g)
#LoadNavSegments("cat_seg.txt", g)
#LoadNavAirports("cat_aer.txt", g)
#per posar el graf dins l'interfaç, importem el FigureCanvasTkAgg
fileAER="cat_aer.txt"
fileNAV="cat_nav"
fileSEG="cat_seg.txt"

def LoadFileAER():
    global fileAER
    ruta_fitxerAER = filedialog.askopenfilename(
        title="Selecciona un fitxer .txt",
        filetypes=[("Fitxers de text", "*.txt")]
    )
    if ruta_fitxerAER:
        print("Has seleccionat:", ruta_fitxerAER)
        with open(ruta_fitxerAER, "r", encoding="utf-8") as fitxer:
            contingut = fitxer.read()
        fileAER="new_data_AER.txt"
        with open(fileAER, "w") as f:
            f.writelines(contingut)


def LoadFileNAV():
    global fileNAV
    ruta_fitxerNAV = filedialog.askopenfilename(
        title="Selecciona un fitxer .txt",
        filetypes=[("Fitxers de text", "*.txt")]
    )
    if ruta_fitxerNAV:
        print("Has seleccionat:", ruta_fitxerNAV)
        with open(ruta_fitxerNAV, "r", encoding="utf-8") as fitxer:
            contingut = fitxer.read()
        fileNAV="new_data_NAV.txt"
        with open(fileNAV, "w") as f:
            f.writelines(contingut)


def LoadFileSEG():
    global fileSEG
    ruta_fitxerSEG = filedialog.askopenfilename(
        title="Selecciona un fitxer .txt",
        filetypes=[("Fitxers de text", "*.txt")]
    )
    if ruta_fitxerSEG:
        print("Has seleccionat:", ruta_fitxerSEG)
        with open(ruta_fitxerSEG, "r", encoding="utf-8") as fitxer:
            contingut = fitxer.read()
        fileSEG="new_data_SEG.txt"
        with open(fileSEG, "w") as f:
            f.writelines(contingut)


def CarregarDades():
    global g
    global fileAER
    global fileNAV
    global fileSEG
    g=AirSpace()
    LoadNavPoints(fileNAV, g)
    LoadNavSegments(fileSEG, g)
    LoadNavAirports(fileAER, g)

def Airspace():
    CarregarDades()
    #destruim l'anterior grafic:
    for widget in right_frame.winfo_children():
        widget.destroy()
    fig = PlotMap(g)
    graf = FigureCanvasTkAgg(fig, master=right_frame)
    graf.draw()
    graf.get_tk_widget().pack(fill="both", expand=True)

def Neighbours():
    CarregarDades()
    neighbour_origin=ent1.get()
    fign = NeighboursMap(g,neighbour_origin)
    #destruim l'anterior grafic:
    for widget in right_frame.winfo_children():
        widget.destroy()
    grafn = FigureCanvasTkAgg(fign, master=right_frame)
    grafn.draw()
    grafn.get_tk_widget().pack(fill="both",expand=True)

def AirportsForShortestPath():
    global SP_origin
    global SP_dest
    info=ent2.get().split(" ")
    print(info)
    SP_origin=info[0]
    SP_dest=info[1]

def ShowSPath():
    CarregarDades()
    AirportsForShortestPath()
    #destruim l'anterior grafic:
    for widget in right_frame.winfo_children():
        widget.destroy()
    path=FindShortestMap(g,SP_origin,SP_dest)
    if path!=None:
        figSP=PlotShortestPath(g,path)
        grafSP=FigureCanvasTkAgg(figSP,master=right_frame)
        grafSP.draw()
        grafSP.get_tk_widget().pack(fill="both",expand=True)

#Mida
root=tk.Tk()
root.geometry("1000x600")
root.title("Interfaç gràfica de l'espai aeri de Catalunya")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)

#columna esquerra
left_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
left_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
left_frame.rowconfigure([0, 1],weight=1)

#mapa cat
frame0=tk.LabelFrame(left_frame,bg="#e8eaf6", bd=2, relief="groove")
frame0.pack(fill="both", expand=True, pady=10, padx=10)
boto0=tk.Button(frame0, text="AIRSPACE", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Airspace)
boto0.pack(fill="x",pady=10)

#frame botons
left_frame1 = tk.LabelFrame(left_frame,bg="#e8eaf6",bd=2, relief="groove")
left_frame1.pack(fill="both", expand=True, pady=10, padx=10)
left_frame.rowconfigure([0, 1, 2], weight=1)

#botó veins
frame1=tk.Frame(left_frame1,bg="#e8eaf6")
frame1.pack(fill="both", expand=True, pady=10, padx=10)
boto1=tk.Button(frame1, text="NEIGHBOURS MAP", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Neighbours)
boto1.pack(fill="x",pady=(0,20))
ent1=tk.Entry(frame1,font=("Segoe UI", 10))
ent1.pack(fill="x",pady=(0,10))

#botó sPath
frame2=tk.Frame(left_frame1,bg="#e8eaf6")
frame2.pack(fill="both", expand=True, pady=10, padx=10)
boto2=tk.Button(frame2, text="SHORTEST PATH", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=ShowSPath)
boto2.pack(fill="x",pady=(0,20))
ent2=tk.Entry(frame2,font=("Segoe UI", 10))
ent2.pack(fill="x",pady=(0,10))

#botó Reach
frame3=tk.Frame(left_frame1,bg="#e8eaf6")
frame3.pack(fill="both", expand=True, pady=10, padx=10)
boto3=tk.Button(frame3, text="REACHABILITY MAP", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Neighbours)
boto3.pack(fill="x",pady=(0,20))
ent3=tk.Entry(frame3,font=("Segoe UI", 10))
ent3.pack(fill="x",pady=(0,10))

#columna dreta
right_frame = tk.Frame(root, bg="#e8eaf6", bd=2, relief="groove")
right_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

#fila sota
low_frame=tk.Frame(root, bg="#e8eaf6", bd=2, relief="groove")
low_frame.grid(row=1, column=0, columnspan=2,sticky="nswe", padx=10, pady=10)
low_frame.columnconfigure([0,1,2],weight=1)

#botó aer
frameAer=tk.Frame(low_frame,bg="#e8eaf6")
frameAer.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
botoAer=tk.Button(frameAer, text="INPUT AIRPORTS FILE", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=LoadFileAER)
botoAer.pack(fill="x",pady=(0,20))

#botó nav
frameNav=tk.Frame(low_frame,bg="#e8eaf6")
frameNav.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)
botoNav=tk.Button(frameNav, text="INPUT NAVIGATION POINTS FILE", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=LoadFileNAV)
botoNav.pack(fill="x",pady=(0,20))

#botó seg
frameSeg=tk.Frame(low_frame,bg="#e8eaf6")
frameSeg.grid(row=0, column=2, sticky="nswe", padx=10, pady=10)
botoSeg=tk.Button(frameSeg, text="IMPORT NAVIGATION SEGMENTS FILE", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=LoadFileSEG)
botoSeg.pack(fill="x",pady=(0,20))

#graf
#fig=PlotMap(g)
#graf=FigureCanvasTkAgg(fig,master=right_frame)
#graf.draw()
#graf.get_tk_widget().pack(fill="both",expand=True)

root.mainloop()