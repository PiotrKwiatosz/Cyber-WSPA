from random import randint, seed

seed(0)
a = []
for i in range(100):
    a.append((randint(0,1000)))

print(a)

from collections import Counter

seed(0)
a = [randint(0, 1000) for i in range(100)]  # Generowanie 100 losowych liczb

# Liczenie wystąpień
counter = Counter(a)

# Wyświetlenie wyników
for number, count in counter.items():
    print(f"Liczba {number} wystąpiła {count} razy")
