def cal(x0, N, iter_num):
    x = x0
    for i in range(iter_num):
        if x==0:
            x += 0.0001
        x = x - (x**2-N)/(2*x)
    return x

if __name__ == "__main__":
    N = float(input("Please input N:"))
    print("sqrt(N)=", round(cal(2, N, 1000), 7))
