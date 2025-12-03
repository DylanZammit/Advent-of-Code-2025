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
    s, idx, m = 0, 0, 12
    for p in range(m-1, -1, -1):
        n = len(digits) if p == 0 else -p
        available = digits[idx:n]
        d = max(available)
        idx = available.index(d) + idx + 1
        s += d * 10 ** p
    out += s
print(out)
submit(out, part="b", day=day, year=year)
