# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

#functions
def drawInNYears(ax, n, m, o):
    n_list = [x for x in range(n)]
    if len(m)<n or len(o)<n:
        raise "Error!Not enough owl or mouse data!"
    sm = m[0:n]
    so = o[0:n]
    ax.plot(n_list, sm, label="mouse", color="red")
    ax.plot(n_list, so, label="owl", color="blue")

def wrap(func):
    global fig, ax1, ax2, ax3, ax4
    def wrap_func(sm, so, A1, A2, B1, B2):
        return func(fig, ax1, ax2, ax3, ax4 ,sm, so, A1, A2, B1, B2)
    return wrap_func
    
@wrap
def rePlot(fig, ax1, ax2, ax3, ax4 ,sm, so, A1, A2, B1, B2):
    '''
Arguments:
    fig : the figure
    ax1,ax2,ax3,ax4 : the axes
    sm : the number of mouses to start
    so : the number of owls to start
    A1,A2,B1,B2 : factors
    '''
    #years
    n1 = 5
    n2 = 30
    n3 = 100
    n4 = 200

    #mouse and owl's numbers' table
    m = [sm]
    o = [so]

    #the length of m and o
    maxN = max(n1, n2, n3, n4)

    #calculate m and o
    for i in range(1, maxN):
        nm = A1 * m[i-1] - A2 * o[i-1] * m[i-1]
        no = B1 * o[i-1] + B2 * m[i-1] * o[i-1]
        if nm < 0 : nm = 0
        if no < 0 : no = 0
        m.append(nm)
        o.append(no)


    #show start value and factors
    fig.suptitle(
                  "A1={0}  A2={1}  mouse={2}\n".format(A1, A2, sm)
                + "B1={0}  B2={1}  owl={2}\n".format(B1, B2, so)
                )

    #clear axes to prepare for rePlots
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    
    #set titles and plot
    ax1.set_title("in {} years".format(n1))
    drawInNYears(ax1, n1, m, o)

    ax2.set_title("in {} years".format(n2))
    drawInNYears(ax2, n2, m, o)

    ax3.set_title("in {} years".format(n3))
    drawInNYears(ax3, n3, m, o)

    ax4.set_title("in {} years".format(n4))
    drawInNYears(ax4, n4, m, o)

    return



#start value and factors
m0 = 156
o0 = 200

A1 = 1.2
A2 = 0.001
B1 = 0.7
B2 = 0.002


#figure create
fig = plt.figure(figsize=(15,10))

#axes create and plot  
ax1 = plt.subplot(221)
ax2 = plt.subplot(222)
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)




#draw
#start_mouse, start_owl, A1, A2, B1, B2
sm = [200, 200, 300, 20]
so = [150, 100, 150, 10]

for i in range(4):
    rePlot(sm[i], so[i], A1, A2, B1, B2)
    ax2.legend(bbox_to_anchor=(1, 1),
            bbox_transform=plt.gcf().transFigure)
    plt.show()
    fig.savefig("D:\\code_concerned\\mypython\\canopy\\{}.png".format(i+1))




#legend and show

