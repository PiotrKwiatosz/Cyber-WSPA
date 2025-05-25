from random import randint, seed

seed(0)
a = []
for i in range(100):
    a.append((randint(0,10)))
#print(a)
#
lista_x=[]
d = {}
for i in range(0,11):
    #print(i,a.count(i))
    d[i] = a.count(i)
    lista_x.append(a.count(i))

#print(lista_x)
print(d)
d[11] = 123
for i in d:
    print(i, d[i])