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

def CarregarDades():
    global g
    g=AirSpace()
    LoadNavPoints("cat_nav", g)
    LoadNavSegments("cat_seg.txt", g)
    LoadNavAirports("cat_aer.txt", g)

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

#columna esquerra
left_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
left_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
left_frame.rowconfigure([0, 1],weight=1)

#mapa cat
frame0=tk.LabelFrame(left_frame,bg="#ffffff")
frame0.pack(fill="both", expand=True, pady=10, padx=10)
boto0=tk.Button(frame0, text="AIRSPACE", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Airspace)
boto0.pack(fill="x",pady=10)

#frame botons
left_frame1 = tk.LabelFrame(left_frame,bg="#ffffff")
left_frame1.pack(fill="both", expand=True, pady=10, padx=10)
left_frame.rowconfigure([0, 1, 2], weight=1)

#botó veins
frame1=tk.Frame(left_frame1,bg="#ffffff")
frame1.pack(fill="both", expand=True, pady=10, padx=10)
boto1=tk.Button(frame1, text="NEIGHBOURS MAP", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Neighbours)
boto1.pack(fill="x",pady=(0,20))
ent1=tk.Entry(frame1,font=("Segoe UI", 10))
ent1.pack(fill="x",pady=(0,10))

#botó sPath
frame2=tk.Frame(left_frame1,bg="#ffffff")
frame2.pack(fill="both", expand=True, pady=10, padx=10)
boto2=tk.Button(frame2, text="SHORTEST PATH", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=ShowSPath)
boto2.pack(fill="x",pady=(0,20))
ent2=tk.Entry(frame2,font=("Segoe UI", 10))
ent2.pack(fill="x",pady=(0,10))

#botó Reach
frame3=tk.Frame(left_frame1,bg="#ffffff")
frame3.pack(fill="both", expand=True, pady=10, padx=10)
boto3=tk.Button(frame3, text="REACHABILITY MAP", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Neighbours)
boto3.pack(fill="x",pady=(0,20))
ent3=tk.Entry(frame3,font=("Segoe UI", 10))
ent3.pack(fill="x",pady=(0,10))

#columna dreta
right_frame = tk.Frame(root, bg="#e8eaf6", bd=2, relief="groove")
right_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

#graf
#fig=PlotMap(g)
#graf=FigureCanvasTkAgg(fig,master=right_frame)
#graf.draw()
#graf.get_tk_widget().pack(fill="both",expand=True)

root.mainloop()