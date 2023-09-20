num = 5
print(id(num))

a = 10
b = a


# Same address because both are having the same value or data
print("The address of a after assigning a = 10",id(a))
print("The address of b after assigning b = a",id(b))
print("Checking the address of the number itself that is 10",id(10))   # Same address because we are having the same number that is 10

a = 9
print("The address of a after reassigning a = 9",id(a))
print("The address of b without reassigning",id(b))
k = a
print("The address of k after assigning k = a",id(k))
b = 8
print("The address b after assigning b = 8",id(b))

print("The address of the number 10 only which has the garbage value",id(10))

# in python we can't assign const but we can show our intentions

x = 18.9
print(type(x))