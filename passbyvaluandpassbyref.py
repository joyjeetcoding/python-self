# Call by value

# def update(x):
#     x = 8
#     print("x = ", x)

# a = 10
# update(a)

# print("a = ", a)


# Call by reference

def update(x):
    x.append(50)
    print("x = ", x)

a = [1, 2, 3, 4]
update(a)

print("a = ", a)