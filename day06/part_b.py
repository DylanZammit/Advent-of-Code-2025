from utils import *
from aocd import get_data, submit
import numpy as np

year, day = 2025, 6

dat = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''
dat = get_data(year=year, day=day, block=True)

eqns, sgns = dat.rsplit('\n', 1)
eqns = '\n'.join(''.join(col) for col in zip(*(line for line in eqns.splitlines())))
eqns = [ints(e) for e in eqns.replace(' ', '').split('\n\n')]
sgns = sgns.replace(' ', '')

out = sum(sum(eqn) if op == '+' else np.prod(eqn) for eqn, op in zip(eqns, sgns))

print(out)
submit(out, part="b", day=day, year=year)
