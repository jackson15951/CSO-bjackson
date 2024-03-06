'''
Corin Chepko
3/26/24
Kattis Problem Roll Call: https://open.kattis.com/problems/rollcall
'''
import sys

def first_name_key(x): return x[0]

names = []
fnames = []

for name in sys.stdin:
    if not name or name == '\n': break
    name = name.strip().split()
    names.append(name)

names.sort(key = first_name_key)
names.sort(key = lambda x:(x[1]))

for name in names: fnames.append(name[0])
for name in names: print(name[0],name[1]) if fnames.count(name[0]) > 1 else print(name[0])