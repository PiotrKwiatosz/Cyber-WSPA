from random import *
import time

aa = []
nn = int(input('podaj nn:'))
seed(0)
t1 = (time.time())
for ii in range(nn):
    aa.append(randint(1,32767))
t2 = time.time()

print('generowanie:', t2 - t1)

#print(aa)
count = 0
t1 = (time.time())
for i in range(nn-1):
    for j in range(nn-i-1):
        if aa[j] > aa[j+1]:
            aa[j], aa[j+1] = aa[j+1], aa[j]

t2 = (time.time())

print('sort: ', t2 - t1)
print('koniec')