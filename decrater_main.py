def validate(func):    
    def inner_function(x):
        if type(x)==type(1):
            result = func(x)
            print("Result ",result)    
        else:
            print("Invalid number")
    return inner_function

@validate
def inc(x):
    return x+1

@validate
def dec(x):
    return x-1

inc(4)
inc("4")