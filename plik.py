plik = open("C:/Users/piotr/OneDrive/Dokumenty/IT/WSPA/GitHub/Cyber-WSPA/dane.txt", "r")
dane = plik.read()
plik.close()
print(dane)
print(type(dane), len(dane))

a = 'aabbddsabbbsssssaaaaaaddddddsssssabds '
b = set(a)
d = {}

for element in b:
    d[element] = a.count(element)

print(b, len(b))

print(d)