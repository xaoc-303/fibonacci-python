import sys
import time

def f1(n):
    return 0 if n == 0 else (1 if n == 1 else f1(n-1) + f1(n-2))

def f2(n):
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b

def start(f, n):
    if f == "f1":
        start = time.time()
        result = f1(n)
        print("{:.8f}".format(time.time() - start))
        return result

    if f == "f2":
        start = time.time()
        result = f2(n)
        print("{:.8f}".format(time.time() - start))
        return result

    return 0

f = sys.argv[1]
n = int(sys.argv[2])

print(start(f, n))
