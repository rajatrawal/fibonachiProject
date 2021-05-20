def fibonachi_v1(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


fib = fibonachi_v1(n=10)
print(fib)
for value in fib:
    print(value)