from utils import *
from aocd import get_data, submit

year, day = 2025, 7

dat = '''.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............'''
dat = get_data(year=year, day=day, block=True)

dat = Grid(dat)

S = next(k for k, v in dat.items() if v == 'S')
@cache
def solve(S):
    out = 0
    dirn = (0, 1)
    p = S
    while (new_pos := add2(dirn, p)) in dat:
        if dat[new_pos] in '.':
            p = new_pos
            continue

        out += 1
        left = add2(new_pos, (-1, 0))
        right = add2(new_pos, (1, 0))

        if left in dat:
            out += solve(left)
        if right in dat:
            out += solve(right)
        break
    return out

out = solve(S) + 1
print(out)
submit(out, part="b", day=day, year=year)
