from random import random
a = [1000,10000,100000,1000000,10000000,100000000]

for ile in a:
    s = 0
    for n in range (ile):
        x = random()
        y = random()
        if x**2+y**2 <=1: s = s+1
    print(ile,  4.0*s/ile)