from tkinter import *
from tkinter import ttk
from math import factorial
from math import *
from itertools import combinations
import itertools

def ya_ne_znau_chto_pridymatb(hot,asS,f):
    po = len(hot.get().split())
    d = asS.get()
    ASs = Label(f, text=f"{po ** d}")
    ASs.pack()

def permutations_with_repetition(n, k_list):
    denominator = 1
    for k in k_list:
        denominator *= factorial(k)
    return factorial(n) // denominator

def comb_rep(elem,r):
    res=itertools.combinations_with_replacement(elem, r)
    return len(res)

def comb(elem):
    res = combinations(elem)
    return len(res)

def perestanovki_s_povt():
    f = Tk()
    Entry1 = ttk.Entry(f)
    Entry1.pack()
    Entry2 = ttk.Entry(f)
    Entry2.pack()
    qwerty = ttk.Button(f, text ="Нажми для вывода результата", command=lambda: ya_ne_znau_chto_pridymatb(Entry1,Entry2,f))
    qwerty.pack()

def razmeshenia():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)
    k = ttk.Entry(m)
    k.pack(anchor=NW, padx=8, pady=8)

    def BUTton_create():
        c = a.get().split()
        d = int(k.get())
        f = Label(m, text=f"{len(c) ** d}")
        f.pack()

    h = ttk.Button(m, text="Нажми для вывода результата", command=BUTton_create)
    h.pack(anchor=NW, padx=8, pady=8)


def perestanovki():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)

    def calculate_factorial():
        c = a.get()
        b = Label(m, text=f"{factorial(len(c))}")
        b.pack()

    calculate_button = ttk.Button(m, text="Нажми для вывода результата", command=calculate_factorial)
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
        d = b.get
        ui = Label(kl, text=f"{permutations_with_repetition(len(c),d)}")
        ui.pack()

    calculate_button = ttk.Button(kl, text="Нажми для вывода результата", command=hfuihfewu)
    calculate_button.pack()
    kl.mainloop()

def ryd(a,kop,j):
        b = len(a.get().split())
        k = int(kop.get())
        Lavel = Label(j, text=f"{comb(b, k)}")
        Lavel.pack()

def sochetania_s_povt():
    j = Tk()
    a = ttk.Entry(j)
    a.pack(anchor=NW, padx=8, pady=8)
    kop = ttk.Entry(j)
    kop.pack()
    d = ttk.Button(j, text="Нажми для вывода результата", command= lambda:ryd(a,kop,j))
    d.pack()
    j.mainloop()

def sochetania_bez_povt():
    j = Tk()
    a = ttk.Entry(j)
    a.pack(anchor=NW, padx=8, pady=8)
    kop = ttk.Entry(j)
    kop.pack()

    def ryd():
        b = a.get().split()
        ass = Label(j, text=f"{comb_rep(b, int(kop.get()))}")
        ass.pack(anchor=CENTER)

    d = ttk.Button(j, text="Нажми для вывода результата", command=ryd)
    d.pack()

    h = ttk.Button(m, text="рассчитать", command=Button_CREate)
    h.pack(anchor=NW, padx=8, pady=8)

root = Tk()
root.title("Калькулятор")
root.geometry("300x250")
button4 = ttk.Button(root, text="перестановки", command=perestanovki)
button4.pack()
button3 = ttk.Button(root, text="размещения", command=razmeshenia)
button3.pack()
button = ttk.Button(text="размещения c повторениями", command=perestanovki_s_povt)
button.pack()
button2 = ttk.Button(root, text="сочетания с повторениями", command=sochetania_s_povt)
button2.pack()
button1 = ttk.Button(root, text="сочетания без повторений", command=sochetania_bez_povt)
button1.pack()
root.mainloop()
