def function():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)
    c = str(a.get)
    k = ttk.Entry(m)
    k.pack(anchor=NW, padx=8, pady=8)
    d = k.get
    def buttons():
        c = a.get()
        g = len(c)
        d = int(k.get())
        hj = fact(g - d)
        fg = fact(g)
        f = Label(m, text=f"{fg / hj}")
        f.pack()
    h = ttk.Button(m, text =" hgtubgthufnr3",command= buttons)
    h.pack(anchor=NW, padx=8, pady=8)
