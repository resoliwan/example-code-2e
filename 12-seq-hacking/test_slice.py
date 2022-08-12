# >>> slice
# <class 'slice'>
# >>> dir(slice)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'indices', 'start', 'step', 'stop']
# >>>
slice.indices
# 'ABCDE'[:10:2] is the same as 'ABCDE'[0:5:2] .

print(slice(0, 10, 2))
# slice(0, 10, 2)
print(slice(0, 10, 2).indices(5))
# (0, 5, 2)
print(slice(-3).indices(5))

# (0, 2, 1)

t = (1, 2, [3, 4])
t[2] += [5, 6]
print(t)
