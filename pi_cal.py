import pdb
from math import sin, pi

K = 6#外推次数，即k的最大值
g = [[None for t in range(K-k)] for k in range(K)]#表

h_0 = 2
for t in range(K):#初始化第一列
    g[0][t] = (2**t/h_0)*sin(h_0*pi/(2**t))
    
for k in range(1, K):
    for t in range(K-k):
        temp = 2**(2*k)
        g[k][t] = (temp*g[k-1][t+1]-g[k-1][t])/(temp-1)

print("    ",end="")
for t in range(K):
    print(t, end="\t")
print()
for k in range(K):
    print("k={}:".format(k), end="")
    for t in range(K-k):
        print(round(g[k][t], 10), end="\t")
    print()
