from functools import lru_cache

@lru_cache(maxsize=None)  # Caches all computed values
def fibr(a):
    if a < 2:
        return a
    return fibr(a - 1) + fibr(a - 2)

for i in range(60):
    print(i, fibr(i))