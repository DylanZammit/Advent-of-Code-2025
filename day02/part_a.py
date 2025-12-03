from utils import *
from aocd import get_data, submit
import re

year, day = 2025, 2

dat = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''
dat = get_data(year=year, day=day, block=True)

dat = [(str(x), str(y)) for x, y in batched(positive_ints(dat), 2)]
out = 0

valid = []
for a, b in dat:
    for c in range(int(a), int(b)+1):
        if re.search(r'^(\d+)\1$', str(c)):
            valid.append(c)

out = sum(valid)
print(out)
submit(out, part="a", day=day, year=year)
