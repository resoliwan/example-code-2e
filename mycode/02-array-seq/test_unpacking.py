# Unpacking Sequence and Iterable
arr = (1, 2)
a, b = arr

val = (10, 3)
div, mod = divmod(*val)

# Using * to grep excess items

a, *body, c = range(4)
# >>> 0 [1, 2] 3

# Unpacking * in function call
def fun(a, b, *rest):
    print(rest)
    # >>> [3, 4, 5]
    return a, b, *rest


a = fun(*[1, 2], *range(3, 6))
print(a)
# >>> 1, 2, 3, 4, 5

a, b, *rest = fun(*[1, 2], *range(3, 6))
print("a, b, rest ", a, b, rest)
# >>> 1 2 [3, 4, 5]
print("a, b, *rest ", a, b, *rest)
# >>> 1 2 3 4 5

# Unpacking Sequence literal
a = *range(1, 3), 3
# >>> (1, 2, 3)
b = {*range(1, 3), 3}
# >>> { 1, 2, 3 }

arr = [(1, 2, (3, 4))]
for a, b, (c, d) in arr:
    print(c, d)
# >>> 3 4
