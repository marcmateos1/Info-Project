from graph import *
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import filedialog
from navAirpoint import NavAirport
from navPoint import NavPoint
from navSegment import NavSegment
import matplotlib.pyplot as plt
from airSpace import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

g=AirSpace()
#per posar el graf dins l'interfaç, importem el FigureCanvasTkAgg

def Neighbours():
    neighbour_origin=entry.get()
    NeighboursMap(g,neighbour_origin)
#Mida
root=tk.Tk()
root.geometry("1000x600")
root.title("Interfaç gràfica de l'espai aeri de Catalunya")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=4)

#columna esquerra
left_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
left_frame.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)
left_frame.rowconfigure([0, 1, 2], weight=1)

#botó veins
frame1=tk.Frame(left_frame,bg="#ffffff")
frame1.pack(fill="both", expand=True, pady=10, padx=10)
boto1=tk.Button(frame1, text="NEIGHBOURS MAP", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Neighbours)
boto1.pack(fill="x",pady=(0,20))
ent1=tk.Entry(frame1,font=("Segoe UI", 10))
ent1.pack(fill="x",pady=(0,10))

#botó sPath
frame2=tk.Frame(left_frame,bg="#ffffff")
frame2.pack(fill="both", expand=True, pady=10, padx=10)
boto2=tk.Button(frame2, text="SHORTEST PATH", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Neighbours)
boto2.pack(fill="x",pady=(0,20))
ent2=tk.Entry(frame2,font=("Segoe UI", 10))
ent2.pack(fill="x",pady=(0,10))

#botó Reach
frame3=tk.Frame(left_frame,bg="#ffffff")
frame3.pack(fill="both", expand=True, pady=10, padx=10)
boto3=tk.Button(frame3, text="REACHABILITY MAP", bg="#007acc", fg="white", font=("Segoe UI", 10, "bold"), relief="flat", height=2, command=Neighbours)
boto3.pack(fill="x",pady=(0,20))
ent3=tk.Entry(frame3,font=("Segoe UI", 10))
ent3.pack(fill="x",pady=(0,10))

#columna dreta
right_frame = tk.Frame(root, bg="#e8eaf6", bd=2, relief="groove")
right_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

#graf
LoadNavPoints("cat_nav", g)
LoadNavSegments("cat_seg.txt", g)
LoadNavAirports("cat_aer.txt", g)

fig=PlotMap(g)
graf=FigureCanvasTkAgg(fig,master=right_frame)
graf.draw()
graf.get_tk_widget().pack(fill="both",expand=True)

root.mainloop()