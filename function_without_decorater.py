def validate(func):    
    def inner_function(x):
        if type(x)==type(1):
            result = func(x)
            print("Result ",result)    
        else:
            print("Invalid number")
    return inner_function

def inc(x):
    return x+1

def dec(x):
    return x-1

validate(inc)(4)
validate(inc)("4")