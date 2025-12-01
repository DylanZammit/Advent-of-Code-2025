from aocd import get_data, submit

year, day = 2025, 1

dat = '''L68
L30
R48
L5
R60
L55
L1
L99
R14
L82'''

dat = get_data(year=year, day=day, block=True)

dat = dat.split('\n')
dial = 50
res = 0

for w in dat:
    s, d = -1 if w[0] == 'L' else 1, int(w[1:])
    dial = (dial + s * d) % 100
    if dial == 0:
        res += 1


print(res)
submit(res, part="a", day=day, year=year)
