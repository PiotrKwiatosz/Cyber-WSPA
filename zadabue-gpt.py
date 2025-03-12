import random

def estimate_pi(n):
    s = 0   #liczba punktow w kole
    for i in range(1, n):
        x, y = random.random(), random.random() #losujemy (x, y) z (0,1)
        if x ** 2 + y ** 2 <= 1: #sprawdzamy, czy punkt jest w cwiartce kola
            s += 1
    z = 4 * s / n
    return z

#testujemy dla roznych wartosci
for n in [1000, 10000, 100000, 1000000]:
    print(estimate_pi(n))
