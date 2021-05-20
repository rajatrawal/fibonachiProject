def fibonachi_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        if a > 10 ** 20:
            return


for val in fibonachi_v3():
    print(val)