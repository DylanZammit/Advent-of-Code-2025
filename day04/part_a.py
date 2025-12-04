from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2025, 4

dat = get_data(year=year, day=day, block=True)
dat2 = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

dat = Grid(dat)

out = 0
for k, v in dat.items():
    if v == '@':
        rop = 0
        success = True
        for dir in directions8:
            if dat.get(add2(dir, k)) == '@':
                rop += 1
                if rop >= 4:
                    success = False
                    break
        if success:
            out += 1

print(out)
submit(out, part="a", day=day, year=year)
