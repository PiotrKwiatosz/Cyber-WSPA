def fibr(a):
    if a == 0: return 0
    if a == 1: return 1
    if a == 2: return 1
    return fibr(a-1) + fibr(a-2)


for i in range(0,100):
    print(i, fibr(i))