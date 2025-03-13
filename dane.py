plik = open("C:/Users/piotr/OneDrive/Dokumenty/IT/WSPA/GitHub/Cyber-WSPA/dane.txt", "r")
dane = plik.read()
plik.close()
dane = dane.split("\n")
#print(set(dane))
#print(dane)
s = set(dane)
d = {}

for e in s:
    d[e] = dane.count(e)
#print(d)

for e in d:
    if d[e] > 1:
        print(e, d[e])

