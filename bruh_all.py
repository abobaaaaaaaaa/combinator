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
def razmeshenia_c_poBtoreniami():
    f = Tk()
    ASSS = ttk.Entry(f)
    ASSS.pack()
    asS = ttk.Entry(f)
    asS.pack()
    def ya_ne_znau_chto_pridymatb():
        po = len(ASSS.get().split())
        d = asS.get()
        ASs = Label(f,text = f"{po**d}")
        ASs.pack()
    qwerty = ttk.Button(f, text ="расчитать количество размещений с повоторениями", command = ya_ne_znau_chto_pridymatb)
    qwerty.pack()



def CUMozin():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)
    k = ttk.Entry(m)
    k.pack(anchor=NW, padx=8, pady=8)

    def IDITE_NAFIG_CO_CBOIMI_NAZBANIAMI():
        c = a.get().split()
        d = int(k.get())
        f = Label(m, text=f"{len(c) ** d}")
        f.pack()

    h = ttk.Button(m, text="hgtubgthufnr3", command=IDITE_NAFIG_CO_CBOIMI_NAZBANIAMI)
    h.pack(anchor=NW, padx=8, pady=8)


def bruh():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)

    def calculate_factorial():
        c = a.get()
        b = Label(m, text=f"{factorial(len(c))}")
        b.pack()

    calculate_button = ttk.Button(m, text="рассчитать количество перестановок", command=calculate_factorial)
    calculate_button.pack()

    m.mainloop()
def igfnjunu():
    kl = Tk()
    a = ttk.Entry(kl)
    a.pack(anchor=NW, padx=8, pady=8)
    b = ttk.Entry(kl)
    b.pack(anchor=NW, padx=8, pady=8)


    def hfuihfewu():
        c = a.get().split()
        d = int(b.get)
        ui = Label(kl, text=f"{permutations_with_repetition(c,d)}")
        ui.pack()

    calculate_button = ttk.Button(kl, text="рассчитать количество перестановок", command=hfuihfewu)
    calculate_button.pack()

    kl.mainloop()

def Rydb():
    j = Tk()
    a = ttk.Entry(j)
    a.pack(anchor=NW, padx=8, pady=8)
    kop = ttk.Entry(j)
    kop.pack()

    def ryd():
        b = a.get().split()
        ass = Label(j, text=f"{comb(b, int(kop.get()))}")
        ass.pack(anchor=CENTER)

    d = ttk.Button(j, text="посчитать сочетания", command=ryd)
    d.pack()

def Bruh():
    j = Tk()
    a = ttk.Entry(j)
    a.pack(anchor=NW, padx=8, pady=8)
    kop = ttk.Entry(j)
    kop.pack()

    def ryd():
        b = a.get().split()
        ass = Label(j, text=f"{comb_rep(b, int(kop.get()))}")
        ass.pack(anchor=CENTER)

    d = ttk.Button(j, text="посчитать сочетания", command=ryd)
    d.pack()
def CUMozin_2():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)
    k = ttk.Entry(m)
    k.pack(anchor=NW, padx=8, pady=8)

    def IDITE_NAFIG_CO_CBOIMI_NAZBANIAMI():
        c = a.get().split()
        d = int(k.get())
        u = factorial(len(c))
        gf =  factorial( len(c) - d)
        f = Label(m, text=f"{u / gf}")
        f.pack()

    h = ttk.Button(m, text="hgtubgthufnr3", command=IDITE_NAFIG_CO_CBOIMI_NAZBANIAMI)
    h.pack(anchor=NW, padx=8, pady=8)


root = Tk()
root.title("Калькулятор")
root.geometry("300x250")

ab = ttk.Button(root, text="перестановки", command=bruh)
ab.pack()
af = ttk.Button(root, text ="перестановки с повторениями", command= igfnjunu)
af.pack()
ac = ttk.Button(root, text="размещения", command=CUMozin)
ac.pack()
ASS = ttk.Button(text ="размещения c повторениями", command= CUMozin_2)
ASS.pack()
ass = ttk.Button(root, text="сочетания", command=Rydb)
ass.pack()
Ass = ttk.Button(root, text = "сочетания 2", command = Bruh)
Ass.pack()
root.mainloop()
