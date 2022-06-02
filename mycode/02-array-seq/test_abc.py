import array

for a in "abc":
    print(a)

symbols = "abc@#$"
codes = [ord(s) for s in symbols]
print(codes)

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

c = [(a_e, b_e) for a_e in a for b_e in b]
print(c)

t = tuple((a_e for a_e in a))
print(t)

arr = array.array("I", (a_e for a_e in a))
print(arr)

a = (10, "abc", (1, 2))
b = (10, "abc", [1, 2])


def hashable(v):
    try:
        hash(v)
    except TypeError:
        return False
    return True


assert hashable(a) is True
assert hashable(b) is False
