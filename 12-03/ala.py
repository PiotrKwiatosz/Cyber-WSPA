import sys

a = '😊'
print(a, ord(a))
print(a.__sizeof__())
print(sys.getsizeof(a))
print(len(a))
print(a.encode("utf-8"))

x = a.encode("utf-8")
print(len(x))


