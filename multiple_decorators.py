def decorator1(func):
    def inner(x):        
        r = func(x)
        print("dec1 ",x,r)
        return r * r
    return inner

def decorator2(func):
    def inner(x):
        r = func(x)
        print("dec2 ",x,r)
        return r * 10
    return inner

@decorator2
@decorator1
def calc(x):
    return x+1

print(calc(4))