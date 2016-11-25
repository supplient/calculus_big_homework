import math

def f1(x):
    return 5*x**9 + 7*x**8 + 10*x**7 + 156*x**4 + 89*x**3 + 90*x**2 + 101*x + 50

def df1(x):
    return 45*x**8 + 56*x**7 + 70*x**6 + 624*x**3 + 267*x**2 + 180*x + 101

def f2(x):
    return x*math.e**x + x**5*math.sin(x**3)

def df2(x):
    return 3*x**7*math.cos(x**3) + 5*x**4*math.sin(x**3) + math.e**x*(x+1)

def cal(x0, iter_num, f, df):
    x = x0
    for i in range(iter_num):
        x = x - f(x)/df(x)
    return x

if __name__ == "__main__":
    print("(1).", round(cal(3, 1000, f1, df1),7))
    print("(2).", round(cal(3, 1000, f2, df2),7))
