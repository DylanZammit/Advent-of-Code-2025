from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2025, 4

dat = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''

dat = get_data(year=year, day=day, block=True)
dat = Grid(dat)

out = 0
out_prev = -1
while out != out_prev:
    out_prev = out
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
                dat[k] = '.'
                out += 1

print(out)
submit(out, part="b", day=day, year=year)
