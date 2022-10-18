# dict comprehendtion
codes = [("key1", "val1"), ("key2", "val2")]

dict = {key: code for key, code in codes}
print(dict)

codes = [("key1", 10), ("key2", 20)]
dict = {key.upper(): code for key, code in sorted(codes) if code > 10}


def dump(**kwargs):
    return kwargs


print(dump(**{"x": 1}, y=2, **{"z": 3}))
print({"x": 1, "z": 1, **{"y": 2, "z": 2}, "y": 3})

d1 = {"x": 1, "y": 1}
d2 = {"y": 2, "z": 2}
print(d1 | d2)
# {'x': 1, 'y': 2, 'z': 2}
