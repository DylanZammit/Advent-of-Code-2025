from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2025, 9

dat = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''
dat = get_data(year=year, day=day, block=True)
dat = [(x, y) for x, y in batched(ints(dat), 2)]
out = max(abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1) for a, b in combinations(dat, 2))
print(out)
submit(out, part="a", day=day, year=year)
