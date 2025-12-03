from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2025, 3

dat = '''987654321111111
811111111111119
234234234234278
818181911112111'''
dat = get_data(year=year, day=day, block=True)

out = 0
for l in dat.split('\n'):
    digits = [int(x) for x in l]
    d1 = max(digits[:-1])
    idx = digits.index(d1)
    d2 = max(digits[idx+1:])
    s = d1*10 +d2
    out += s
print(out)
submit(out, part="a", day=day, year=year)
