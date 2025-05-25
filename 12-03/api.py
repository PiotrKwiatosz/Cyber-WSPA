import requests

waluta = "euro"
kurs = 1.24
print(f" {waluta}, {kurs}")

code = "usd"
x = "2023-01-05"

dane = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{code}/{x}/")
print(dane)

ile = dane.json()
print("coś:", ile)
print(ile["rates"][0]["mid"])
#
for i in range(2022,2024):
    for j in range(12,16):
        x = str(i)+"-"+"12"+"-"+str(j)
        print(x)
        x = "2023-01-05"
        dane = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{code}/{x}/")
        ile = dane.json()
        print(ile["rates"][0]["mid"])