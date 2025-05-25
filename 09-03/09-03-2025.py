def cos(a):
    print('w srodku:', a, id(a))
    a = [11, 22, 44]
    print('w srodku2:', a, id(a))

x = [1, 2, 3]
print('glowny:', x, id(x))
cos(x)
print('glowny2:', x, id(x))