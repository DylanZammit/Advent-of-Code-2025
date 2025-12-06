from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2025, 5

dat = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''
dat = get_data(year=year, day=day, block=True)

ranges, ing = dat.split('\n\n')
ranges = [(x, y) for x, y in batched(positive_ints(ranges), 2)]
ing = positive_ints(ing)

out = len([i for i in ing if any(a <= i <= c for a, c in ranges)])

print(out)
submit(out, part="a", day=day, year=year)
