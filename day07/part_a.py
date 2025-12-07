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
    dirn = (0, 1)
    p = S
    splits = set()
    while (new_pos := add2(dirn, p)) in dat:

        if dat[new_pos] in '.|':
            p = new_pos
            continue

        splits.add(p)
        left = add2(new_pos, (-1, 0))
        right = add2(new_pos, (1, 0))

        if left in dat:
            splits = splits.union(solve(left))
        if right in dat:
            splits.add(right)
            splits = splits.union(solve(right))
        break
    return splits

splits = solve(S)
out = len(splits) // 2
print(out)
submit(out, part="a", day=day, year=year)
