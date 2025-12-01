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
    s, d = w[0], int(w[1:])
    s = -1 if s == 'L' else 1

    res += d // 100
    rem = d % 100
    d = rem
    if d >= dial and s == -1 or d >= (100 - dial) and s == 1:
        res += (1 - dial == 0)

    dial = (dial + s * d) % 100


print(res)
submit(res, part="b", day=day, year=year)
