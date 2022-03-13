def f1(n):
    return 0 if n == 0 else (1 if n == 1 else f1(n-1) + f1(n-2))

def f2(n):
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b
