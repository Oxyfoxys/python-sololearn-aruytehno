# In java:



def fibonacci(n):
    k = 1
    d = 1
    out = 1
    print(0)
    for i in range(n):
        if out < n:
            print(k)
            out += 1
        if out < n:
            print(d)
            out += 1
        k += d
        d += k


fibonacci(10)
