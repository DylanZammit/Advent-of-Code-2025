# Advent-of-Code-2025
## Day 1
### Part A
Simple modulo arithmetic, the magic is done here
```python
dial = (dial + s * d) % 100
```
### Part B
Denote the turn amount by `T`. There are two things to consider.
1. The number of full rotations calculated by `T // 100`.
2. From what remains we check if the distance is exceeded by `T`.
The sum of these two is the answer.
## Day 2
Both parts are brute force. We check all numbers in all of the ranges, and apply the following regex on each number.
```regexp
r'^(\d+)\1+$
 ```
This regex matches a set of digits, and ensure that this first captured group is repeated at least once until the end of the number.
For part A, we simply remove the `+`.
## Day 3
### Part A
### Part B
## Day 4
### Part A
### Part B
## Day 5
### Part A
### Part B
## Day 6
### Part A
### Part B
## Day 7
### Part A
### Part B
## Day 8
### Part A
### Part B
## Day 9
### Part A
### Part B
## Day 10
### Part A
### Part B
## Day 11
### Part A
### Part B
## Day 12
### Part A
### Part B
