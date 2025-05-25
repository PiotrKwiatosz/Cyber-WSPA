def fib(n):
    fib_numbers = [0, 1]  # Pierwsze dwie liczby Fibonacciego
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    return fib_numbers[n]

n = 60
print(f"Liczba Fibonacciego dla {n} to:", fib(n))