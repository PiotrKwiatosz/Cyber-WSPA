def fib(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, "->", fib(n))