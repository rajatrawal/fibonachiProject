def fibonachi_v2():
    a, b = 1, 0
    while True:
        yield a
        a, b = b, a + b


for value in fibonachi_v2():
    print(value)
    if value > 10 ** 5:
        break
