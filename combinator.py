from tkinter import *
from tkinter import ttk
from math import factorial
from math import *
from itertools import combinations
import itertools


def permutations_with_repetition(n, k_list):
    denominator = 1
    for k in k_list:
        denominator *= factorial(k)
    return factorial(n) // denominator
def comb_rep(elem,r):
    res=itertools.combinations_with_replacement(elem, r)
    return len(res)
def comb(elem, r):
    res = combinations(elem, r)
    return len(res)
def placements_with_repetitions():
    f = Tk()
    Entry1 = ttk.Entry(f)
    Entry1.pack()
    Entry2 = ttk.Entry(f)
    Entry2.pack()
    def buTTon_create():
        po = len(Entry1.get().split())
        d = Entry2.get()
        Lavel = Label(f,text = f"{po**d}")
    Lavel.pack()
    o = ttk.Button(f, text ="расчитать количество размещений с повоторениями", command = buTTon_create)
    o.pack()



def placement():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)
    k = ttk.Entry(m)
    k.pack(anchor=NW, padx=8, pady=8)

    def create_BUtton():
        c = a.get().split()
        d = int(k.get())
        f = Label(m, text=f"{len(c) ** d}")
        f.pack()

    h = ttk.Button(m, text="hgtubgthufnr3", command=create_BUtton)
    h.pack(anchor=NW, padx=8, pady=8)


def permutations_calculate():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)

    def calculate_permutations():
        c = a.get()
        b = Label(m, text=f"{factorial(len(c))}")
        b.pack()

    calculate_button = ttk.Button(m, text="рассчитать количество перестановок", command=calculate_permutations)
    calculate_button.pack()

    m.mainloop()
def replaces2():
    kl = Tk()
    a = ttk.Entry(kl)
    a.pack(anchor=NW, padx=8, pady=8)
    b = ttk.Entry(kl)
    b.pack(anchor=NW, padx=8, pady=8)


    def create_bUttton():
        c = a.get().split()
        d = int(b.get)
        ui = Label(kl, text=f"{permutations_with_repetition(c,d)}")
        ui.pack()

    calculate_button = ttk.Button(kl, text="рассчитать количество перестановок", command=create_bUtton)
    calculate_button.pack()

    kl.mainloop()

def combinations():
    j = Tk()
    a = ttk.Entry(j)
    a.pack(anchor=NW, padx=8, pady=8)
    kop = ttk.Entry(j)
    kop.pack()

    def crEAte_button():
        b = a.get().split()
        Lavel = Label(j, text=f"{comb(b, int(kop.get()))}")
        Lavel.pack(anchor=CENTER)

    d = ttk.Button(j, text="посчитать сочетания", command=crEAte_button)
    d.pack()

def replaces():
    j = Tk()
    a = ttk.Entry(j)
    a.pack(anchor=NW, padx=8, pady=8)
    Entry1 = ttk.Entry(j)
    Entry1.pack()

    def button_creatE():
        b = a.get().split()
        Lavel = Label(j, text=f"{comb_rep(b, int(kop.get()))}")
        Lavel.pack(anchor=CENTER)

    d = ttk.Button(j, text="посчитать сочетания", command=button_creatE)
    d.pack()
def placement_2():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)
    k = ttk.Entry(m)
    k.pack(anchor=NW, padx=8, pady=8)

    def button_create():
        c = a.get().split()
        d = int(k.get())
        u = factorial(len(c))
        gf =  factorial( len(c) - d)
        f = Label(m, text=f"{u / gf}")
        f.pack()

    h = ttk.Button(m, text="hgtubgthufnr3", command=button_create)
    h.pack(anchor=NW, padx=8, pady=8)


root = Tk()
root.title("Калькулятор")
root.geometry("300x250")

ab = ttk.Button(root, text="перестановки", command=replaces)
ab.pack()
af = ttk.Button(root, text ="перестановки с повторениями", command= replaces2)
af.pack()
ac = ttk.Button(root, text="размещения", command=CUMozin)
ac.pack()
ty = ttk.Button(text ="размещения c повторениями", command= )
ty.pack()
button = ttk.Button(root, text="сочетания", command=Rydb)
button.pack()
button1 = ttk.Button(root, text = "сочетания 2", command = Bruh)
button1.pack()
button1.mainloop()
