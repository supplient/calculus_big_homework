from math import log

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

def cal_delta(a, b, per):
    dm = log(abs(a[0]-b[0])/per)/log(10)
    do = log(abs(a[1]-b[1])/per)/log(10)
    return (round(dm,2), round(do,2))

def lay_fac_deltas(years, sm, so):
    std = [1.2, 0.001, 0.7, 0.002]
    deltas = {}
    bigPer = 0.1
    smallPer = 0.001
    
    std_res = gen_past(years, *std, sm, so)

    #A1
    fac = [x for x in std]
    fac[0] += bigPer
    fac_res = gen_past(years, *fac, sm, so)
    deltas["A1 positive delta"] = cal_delta(fac_res, std_res, bigPer)
    fac[0] -= bigPer*2
    fac_res = gen_past(years, *fac, sm, so)
    deltas["A1 negative delta"] = cal_delta(fac_res, std_res, bigPer)

    #A2
    fac = [x for x in std]
    fac[1] += smallPer
    fac_res = gen_past(years, *fac, sm, so)
    deltas["A2 positive delta"] = cal_delta(fac_res, std_res, smallPer)
    fac[1] -= smallPer*2
    fac_res = gen_past(years, *fac, sm, so)
    deltas["A2 negative delta"] = cal_delta(fac_res, std_res, smallPer)

    #B1
    fac = [x for x in std]
    fac[2] += bigPer
    fac_res = gen_past(years, *fac, sm, so)
    deltas["B1 positive delta"] = cal_delta(fac_res, std_res, bigPer)
    fac[2] -= bigPer*2
    fac_res = gen_past(years, *fac, sm, so)
    deltas["B1 negative delta"] = cal_delta(fac_res, std_res, bigPer)

    #B2
    fac = [x for x in std]
    fac[3] += smallPer
    fac_res = gen_past(years, *fac, sm, so)
    deltas["B2 positive delta"] = cal_delta(fac_res, std_res, smallPer)
    fac[3] -= smallPer*2
    fac_res = gen_past(years, *fac, sm, so)
    deltas["B2 negative delta"] = cal_delta(fac_res, std_res, smallPer)
    
    return deltas


def lay_start_deltas(years, A1, A2, B1, B2):
    std = [150, 200]
    deltas = {}
    per = 10

    std_res = gen_past(years, A1, A2, B1, B2, *std)

    #mouse
    fac = [x for x in std]
    fac[0] += per
    fac_res = gen_past(years, A1, A2, B1, B2, *fac)
    deltas["Mouse positive delta"] = cal_delta(fac_res, std_res, per)
    fac[0] -= per*2
    fac_res = gen_past(years, A1, A2, B1, B2, *fac)
    deltas["Mouse negative delta"] = cal_delta(fac_res, std_res, per)

    #owl
    fac = [x for x in std]
    fac[1] += per
    fac_res = gen_past(years, A1, A2, B1, B2, *fac)
    deltas["Owl positive delta"] = cal_delta(fac_res, std_res, per)
    fac[1] -= per*2
    fac_res = gen_past(years, A1, A2, B1, B2, *fac)
    deltas["Owl negative delta"] = cal_delta(fac_res, std_res, per)

    return deltas
    

deltas = lay_fac_deltas(100, 150, 200)
for d in deltas:
    print("{}&{}&{}\\\\\n\\hline".format(d, deltas[d][0], deltas[d][1]))

deltas = lay_start_deltas(100, 1.2, 0.001, 0.7, 0.002)
for d in deltas:
    print("{}&{}&{}\\\\\n\\hline".format(d, deltas[d][0], deltas[d][1]))

