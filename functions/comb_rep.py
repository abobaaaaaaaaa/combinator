def comb_rep(elem,r):
    res=itertools.combinations_with_replacement(elem, r)
    return len(res)

