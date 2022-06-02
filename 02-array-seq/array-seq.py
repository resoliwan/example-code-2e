#!/usr/bin/env python
# coding: utf-8

# # Chapter 2 — An Array of Sequences
#
# **Sections with code snippets in this chapter:**
#
# * [List Comprehensions and Generator Expressions](#List-Comprehensions-and-Generator-Expressions)
# * [Slicing](#Slicing)
# * [Building Lists of Lists](#Building-Lists-of-Lists)
# * [Augmented Assignment with Sequences](#Augmented-Assignment-with-Sequences)
# * [list.sort and the sorted Built-In Function](#list.sort-and-the-sorted-Built-In-Function)
# * [Managing Ordered Sequences with bisect](#Managing-Ordered-Sequences-with-bisect)
# * [Arrays](#Arrays)
# * [Memory Views](#Memory-Views)
# * [NumPy and SciPy](#NumPy-and-SciPy)
# * [Deques and Other Queues](#Deques-and-Other-Queues)
# * [Soapbox](#Soapbox)

# ## List Comprehensions and Generator Expressions

# #### Example 2-1. Build a list of Unicode codepoints from a string

# In[1]:


symbols = "$¢£¥€¤"
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

codes


# #### Example 2-2. Build a list of Unicode codepoints from a string, take 2

# In[2]:


symbols = "$¢£¥€¤"

codes = [ord(symbol) for symbol in symbols]

codes


# #### Box: Listcomps No Longer Leak Their Variables

# In[3]:


x = "ABC"
codes = [ord(x) for x in x]
x


# In[4]:


codes


# #### Example 2-3. The same list built by a listcomp and a map/filter composition

# In[5]:


symbols = "$¢£¥€¤"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii


# In[6]:


beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii


# #### Example 2-4. Cartesian product using a list comprehension

# In[7]:


colors = ["black", "white"]
sizes = ["S", "M", "L"]
tshirts = [(color, size) for color in colors for size in sizes]
tshirts


# In[8]:


for color in colors:
    for size in sizes:
        print((color, size))


# In[9]:


shirts = [(color, size) for size in sizes for color in colors]
tshirts


# #### Example 2-5. Initializing a tuple and an array from a generator expression

# In[10]:


symbols = "$¢£¥€¤"
tuple(ord(symbol) for symbol in symbols)


# In[11]:


import array

array.array("I", (ord(symbol) for symbol in symbols))


# #### Example 2-6. Cartesian product in a generator expression

# In[12]:


colors = ["black", "white"]
sizes = ["S", "M", "L"]

for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
    print(tshirt)


# ## Slicing

# ### Why Slices and Range Exclude the Last Item

# In[13]:


l = [10, 20, 30, 40, 50, 60]

l[:2]  # split at 2


# In[14]:


l[2:]


# In[15]:


l[:3]  # split at 3


# In[16]:


l[3:]


# ### Slice Objects

# In[17]:


s = "bicycle"
s[::3]


# In[18]:


s[::-1]


# In[19]:


s[::-2]


# #### Example 2-9. Line items from a flat-file invoice

# In[20]:


invoice = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella                      $17.50    3    $52.50
1489 6mm Tactile Switch x20                  $4.95    2    $9.90
1510 Panavise Jr. - PV-201                  $28.00    1    $28.00
1601 PiTFT Mini Kit 320x240                 $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split("\n")[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


# ### Assigning to Slices

# In[21]:


l = list(range(10))
l


# In[22]:


l[2:5] = [20, 30]
l


# In[23]:


del l[5:7]
l


# In[24]:


l[3::2] = [11, 22]
l


# By design, this example raises an exception::

# In[25]:


try:
    l[2:5] = 100
except TypeError as e:
    print(repr(e))


# In[26]:


l[2:5] = [100]
l


# ### Using + and * with Sequences

# In[27]:


l = [1, 2, 3]
l * 5


# In[28]:


5 * "abcd"


# ### Building Lists of Lists

# #### Example 2-10. A list with three lists of length 3 can represent a tic-tac-toe board

# In[29]:


board = [["_"] * 3 for i in range(3)]
board


# In[30]:


board[1][2] = "X"
board


# #### Example 2-11. A list with three references to the same list is useless

# In[31]:


weird_board = [["_"] * 3] * 3
weird_board


# In[32]:


weird_board[1][2] = "O"
weird_board


# #### Explanation

# In[33]:


board = []
for i in range(3):
    row = ["_"] * 3
    board.append(row)
board


# In[34]:


board[2][0] = "X"
board


# ## Augmented Assignment with Sequences

# In[35]:


l = [1, 2, 3]
idl = id(l)


# In[36]:


# NBVAL_IGNORE_OUTPUT
idl


# In[37]:


l *= 2
l


# In[38]:


id(l) == idl  # same list


# In[39]:


t = (1, 2, 3)
idt = id(t)


# In[40]:


# NBVAL_IGNORE_OUTPUT
idt


# In[41]:


t *= 2
id(t) == idt  # new tuple


# ### A += Assignment Puzzler

# In[42]:


t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except TypeError as e:
    print(repr(e))


# In[43]:


t


# #### Example 2-14. Bytecode for the expression s[a] += b

# In[44]:


import dis

dis.dis("s[a] += b")


# ## list.sort and the sorted Built-In Function

# In[45]:


fruits = ["grape", "raspberry", "apple", "banana"]
sorted(fruits)


# In[46]:


fruits


# In[47]:


sorted(fruits, reverse=True)


# In[48]:


sorted(fruits, key=len)


# In[49]:


sorted(fruits, key=len, reverse=True)


# In[50]:


fruits


# In[51]:


fruits.sort()
fruits


# ## Managing Ordered Sequences with bisect

# #### Example 2-15. bisect finds insertion points for items in a sorted sequence

# In[52]:


# BEGIN BISECT_DEMO
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = "{0:2d} @ {1:2d}    {2}{0:<2d}"


def demo(haystack, needles, bisect_fn):
    print("DEMO:", bisect_fn.__name__)  # <1>
    print("haystack ->", " ".join("%2d" % n for n in haystack))
    for needle in reversed(needles):
        position = bisect_fn(haystack, needle)  # <2>
        offset = position * "  |"  # <3>
        print(ROW_FMT.format(needle, position, offset))  # <4>


demo(HAYSTACK, NEEDLES, bisect.bisect)  # <5>
# END BISECT_DEMO


# In[53]:


demo(HAYSTACK, NEEDLES, bisect.bisect_left)


# #### Example 2-16. Given a test score, grade returns the corresponding letter grade

# In[54]:


def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


[grade(score) for score in [55, 60, 65, 70, 75, 80, 85, 90, 95]]


# #### Example 2-17. bisect_left maps a score of 60 to grade F, not D as in Example 2-16.

# In[55]:


def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    i = bisect.bisect_left(breakpoints, score)
    return grades[i]


[grade(score) for score in [55, 60, 65, 70, 75, 80, 85, 90, 95]]


# #### Example 2-18. Insort keeps a sorted sequence always sorted

# In[56]:


import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print(f"insert {new_item:2d} -> {my_list}")


# ## When a List Is Not the Answer

# ### Arrays

# #### Example 2-19. Creating, saving, and loading a large array of floats

# In[57]:


from array import array
from random import random

floats = array("d", (random() for i in range(10**7)))
floats[-1]


# In[58]:


with open("floats.bin", "wb") as fp:
    floats.tofile(fp)


# In[59]:


floats2 = array("d")

with open("floats.bin", "rb") as fp:
    floats2.fromfile(fp, 10**7)

floats2[-1]


# In[60]:


floats2 == floats


# ### Memory Views

# #### Example 2-20. Changing the value of an array item by poking one of its bytes

# In[61]:


numbers = array("h", [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
len(memv)


# In[62]:


memv[0]


# In[63]:


memv_oct = memv.cast("B")
memv_oct.tolist()


# In[64]:


memv_oct[5] = 4
numbers


# ### NumPy and SciPy

# #### Example 2-21. Basic operations with rows and columns in a numpy.ndarray

# In[65]:


import numpy as np

a = np.arange(12)
a


# In[66]:


type(a)


# In[67]:


a.shape


# In[68]:


a.shape = 3, 4
a


# In[69]:


a[2]


# In[70]:


a[2, 1]


# In[71]:


a[:, 1]


# In[72]:


a.transpose()


# #### Example 2-22. Loading, saving, and vectorized operations

# In[73]:


with open("floats-1M-lines.txt", "wt") as fp:
    for _ in range(1_000_000):
        fp.write(f"{random()}\n")


# In[74]:


floats = np.loadtxt("floats-1M-lines.txt")


# In[75]:


floats[-3:]


# In[76]:


floats *= 0.5
floats[-3:]


# In[77]:


from time import perf_counter as pc

t0 = pc()
floats /= 3
(pc() - t0) < 0.01


# In[78]:


np.save("floats-1M", floats)
floats2 = np.load("floats-1M.npy", "r+")
floats2 *= 6


# In[79]:


floats2[-3:]


# ### Deques and Other Queues

# #### Example 2-22. Working with a deque

# In[80]:


import collections

dq = collections.deque(range(10), maxlen=10)
dq


# In[81]:


dq.rotate(3)
dq


# In[82]:


dq.rotate(-4)
dq


# In[83]:


dq.appendleft(-1)
dq


# In[84]:


dq.extend([11, 22, 33])
dq


# In[85]:


dq.extendleft([10, 20, 30, 40])
dq


# ## Soapbox

# ### Mixed bag lists

# In[86]:


l = [28, 14, "28", 5, "9", "1", 0, 6, "23", 19]


# In[87]:


try:
    sorted(l)
except TypeError as e:
    print(repr(e))


# ### Key is Brilliant

# In[88]:


l = [28, 14, "28", 5, "9", "1", 0, 6, "23", 19]

sorted(l, key=int)


# In[89]:


sorted(l, key=str)


# In[ ]:
