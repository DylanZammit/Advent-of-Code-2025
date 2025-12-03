from utils import *
from aocd import get_data, submit

year, day = 2025, 2

dat = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124'''
dat = get_data(year=year, day=day, block=True)

dat = [(str(x), str(y)) for x, y in batched(positive_ints(dat), 2)]
out = 0

valid = []
for a, b in dat:
    na, nb = len(a), len(b)
    if na == nb and na % 2 == 1:
        continue
    if na % 2 == 1:
        x = int(10 ** na / 10 ** ((na+1) / 2))
    else:
        x = int(a[:na//2])

    while True:
        z = int(str(x) + str(x))
        if z < int(a):
            x += 1
            continue
        if z > int(b):
            break
        assert int(a) <= z <= int(b)
        valid.append(z)
        x += 1

out = sum(valid)
print(out)
submit(out, part="a", day=day, year=year)
