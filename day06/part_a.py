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
eqns = list(zip(*[ints(eqn) for eqn in eqns.split('\n')]))
sgns = sgns.replace(' ', '')

out = sum(sum(eqn) if op == '+' else np.prod(eqn) for eqn, op in zip(eqns, sgns))
print(out)
submit(out, part="a", day=day, year=year)
