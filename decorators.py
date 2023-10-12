def div(a, b):
    if a < b:
        a,b=b,a
     
    print(a/b)

def smartDiv(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner

div(2, 4)