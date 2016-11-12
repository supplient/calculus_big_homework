def gen_past(years, A1, A2, B1, B2, m0, o0):
    m = m0
    o = o0
    nm = 0
    no = 0
    for i in range(1, years):
        nm = A1 * m - A2 * o * m
        no = B1 * o + B2 * m * o
        if nm<0:
            return (0,0)
        if no<0:
            return (m,0)
        m = nm
        o = no
    return (nm, no)

#coexisting system & survival system
def search_coe_sur_system(A1, A2, B1, B2):
    clist = []
    slist = []
    for m in range(1, 1000):
        for o in range(1, 1000):
            (rm, ro)=gen_past(1000, A1, A2, B1, B2, m, o)
            if rm>0 and ro>0:
                clist.append((m, o))
            elif rm>0:
                slist.append((m, o))
    return (clist, slist)

factors = [
    (1.2, 0.001, 0.7, 0.002),
    (1.3, 0.002, 0.8, 0.003),
    (1.1, 0.0015, 0.6, 0.001),
    (1.2, 0.0005, 0.65, 0.0025)
    ]
for fac in factors:
    clist, slist = search_coe_sur_system(*fac)
    res_str="{}&{}&{}&{}".format(*fac)
    for s in clist:
        res_str += '&'+str(s[0])+'&'+str(s[1])
    for s in slist:
        res_str += '&'+str(s[0])+'&'+str(s[1])
    print(res_str)
print("End")



