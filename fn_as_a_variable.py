def inc(x):
    return x+1

def dec(x):
    return x-1

x = inc(4)
print(x)

x = dec(5)
print(x)

def operate(func,x):
    if type(x) != type('str'):
        result = func(x)
        return result

x= operate(inc, x)
print(x)
x= operate(inc, x)
print(x)
x= operate(dec, x)
print(x)

x= operate(dec, "x")
print(x)

