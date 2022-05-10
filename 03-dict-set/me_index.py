import sys
import re

# python my_index.py zen.txt
#
# in
# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# out
# The [(1, 1)]

# file_name = sys.argv[1]

file_name = "/Users/younlee/workspace/fluent_python/03-dict-set/zen.txt"

WORD_RE = re.compile(r"\w+")
index = {}
with open(file_name, encoding="utf-8") as f:
    for line_no, line in enumerate(f, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
