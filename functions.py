def greet():
    print("Hello")
    print("Good Morning")

def add(a, b):
    c = a + b
    # print(c)
    return c

def add_sub(a,b):
    sub = a - b
    add = a + b
    return add, sub


greet()

# result = add(2, 5)

res1, res2 = add_sub(5, 4)

print(res2)