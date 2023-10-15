def div(a, b): 
    print(a/b)

#using decorators we can add extra features for the existing function
def smartDiv(func):     #taking function as a parameter
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div = smartDiv(div)

div(2, 4)

