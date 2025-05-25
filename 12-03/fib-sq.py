def fibi(a):
    a1 = 0
    a2 = 1
    for i in range(0,a):
        a3 = a2 + a1
        a1 = a2
        a2 = a3
    return a1

def fibr(a):
    if a == 0: return 0
    if a == 1: return 1
    if a == 2: return 2
    return fibr(a-1) + fibr(a-2)

for i in range(0,1000):
    print(i, fibi(i))