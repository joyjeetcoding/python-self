# none -> not assigned with any value
# numeric -> int, float, complex, bool

# float
# num = 2.5
# print(type(num))

# int
# num = 5
# print(type(num))

# complex
# num = a+bj
num = 6 + 9j
# print(type(num))

a = 5.6
b = int(a)  #converted to int
# print(type(b))

k = float(b) #converted to float
# print(type(k))

k = 6
c = complex(b, k) #converted to complex
# print(c)
# print(type(c))

# print(b > k)


# ------- Sequence -----------

# list
# tuple
# set
# String
str = "Joyjeet"
st = 'a'
# print(type(st))
# python have string, they don't have char to be specific
# range
print(range(10))
print(list(range(10)))
print(list(range(2, 10, 2)))

# -------- Sequence ends ----------

# dictionary
d = {'joy':'samsung','rahul':'iphone', 'kiran': '1+'}

print(d.keys())
print(d.values())
print(d.get('kiran'))
print(d['kiran'])