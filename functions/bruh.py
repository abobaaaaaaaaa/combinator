def CUMozin():
    m = Tk()
    a = ttk.Entry(m)
    a.pack(anchor=NW, padx=8, pady=8)
    c = str(a.get)
    k = ttk.Entry(m)
    k.pack(anchor=NW, padx=8, pady=8)
    d = k.get
    def IDITE_NAFIG_CO_CBOIMI_NAZBANIAMI():
        c = a.get()
        d = int(k.get())
        f = Label(m, text=f"{factorial(len(c) - d)}")
        f.pack()
    h = ttk.Button(m, text =" hgtubgthufnr3",command= IDITE_NAFIG_CO_CBOIMI_NAZBANIAMI)
    h.pack(anchor=NW, padx=8, pady=8)
