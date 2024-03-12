def comb_rep(matr):
    res = []
    elem = 0
    comb = 0
    val=0
    for i in range(len(matr)):
        res.append(matr[elem])
        while comb < len(matr):
            res.append(matr[comb])
            res.pop()
            comb += 1
        val+=1
        res.clear()
        elem += 1
        comb = 0
    return val
