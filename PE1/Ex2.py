def func_1(a):
    return a ** a
 
 
def func_2(a):
    return func_1(a) * func_1(a)
 
 
print(func_2(2))