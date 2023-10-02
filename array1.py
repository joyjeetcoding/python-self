# * means you want to work with all the functions
from array import *

vals = array('i',[2, 9, 8, 4, 5])
# here 'i' is typecode

# -ve values can be there in arrays but we will use use decimal it must be converted to 'f'

# vals = array('i',[5, 9, 8, 4, 2])
# vals = array('f',[5.5, 9, 8, 4, 2])

# vals.reverse()

for i in range(len(vals)):
    print(vals[i])

# for i in range(5):
#     print(vals[i])
# print(vals[0])