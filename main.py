import sys
import time
import fibo

def start(f, n):
    if f == "f1":
        start = time.time()
        result = fibo.f1(n)
        print("{:.8f}".format(time.time() - start))
        return result

    if f == "f2":
        start = time.time()
        result = fibo.f2(n)
        print("{:.8f}".format(time.time() - start))
        return result

    return 0

f = sys.argv[1]
n = int(sys.argv[2])

print(start(f, n))
