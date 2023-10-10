from functools import reduce

# def is_even(n):
#     return n % 2 == 0

def update(n):
    return n*2

def add_all(a, b):
    return a+b

nums = [3, 2, 6, 8, 4, 6, 2, 9]

# filter()



# evens = list(filter(is_even, nums))
evens = list(filter(lambda n : n % 2 == 0, nums))




# map()


# doubles = list(map(update, evens))

doubles = list(map(lambda n : n * 2, evens))



# reduce()

# sum = reduce(add_all, doubles)
sum = reduce(lambda a,b: a+b, doubles)


print(sum)
