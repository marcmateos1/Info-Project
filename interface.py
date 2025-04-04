import tkinter as tk

import matplotlib.pyplot as plt

#li donem  mida i títol a la finestra i creem les files i columnes necessàries
fin=tk.Tk()
fin.geometry("800x400")
fin.title("graphs")
fin.columnconfigure(0)
fin.columnconfigure(1)
fin.rowconfigure(0)
fin.rowconfigure(1)
fin.rowconfigure(2)

q1=tk.LabelFrame(fin,text="Choose graph:")
q1.grid(row=0,column=0,pady=10,padx=10,sticky=tk.N + tk.E + tk.W + tk.S)

fin.mainloop()