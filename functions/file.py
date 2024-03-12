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
        d = int(k.get())
        f = Label(m, text=f"{factorial(len(c) - d)}")
        f.pack()
    h = ttk.Button(m, text =" hgtubgthufnr3",command= buttons)
    h.pack(anchor=NW, padx=8, pady=8)
