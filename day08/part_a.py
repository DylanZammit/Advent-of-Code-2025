from utils import *
from aocd import get_data, submit
from itertools import combinations

year, day = 2025, 8

dat = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''
dat = get_data(year=year, day=day, block=True)

dat = {(x, y, z): ((0,0,0), np.inf) for x, y, z in batched(ints(dat), 3)}
res = {}
dists = {}

for a, b in combinations(dat, 2):
    if a == b: continue
    dists[(a, b)] = np.linalg.norm(np.array(a) - np.array(b))

closest_boxes = [k for k, v in sorted(dists.items(), key=lambda item: item[1])]

N = 1000
clusters = {a: {a} for a in dat}
for i, (a, b) in enumerate(closest_boxes):
    if i >= N:
        break
    clusters[a].add(b)
    clusters[b].add(a)

for a in clusters:
    for b in clusters:
        if clusters[a].intersection(clusters[b]):
            clusters[a] = clusters[a].union(clusters[b])
            clusters[b] = clusters[a]

clusters = set([frozenset(v) for v in clusters.values()])
lens = sorted([len(c) for c in clusters])
out = int(np.prod(lens[-3:]))

print(out)
submit(out, part="a", day=day, year=year)
