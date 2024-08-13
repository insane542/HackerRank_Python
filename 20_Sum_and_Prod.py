"""
Task:
You are given a 2-D array with dimensions N X M.
Your task is to perform the sum tool over axis 0 and then find the product of that result.

Input Format:
The first line of input contains space separated values of N and M.
The next Nlines contains M space separated integers.

Output Format:
Compute the sum along axis 0. Then, print the product of that sum.

Sample Input:
2 2
1 2
3 4

Sample Output:
24

Explanation:
The sum along axis 0 = [4 6]
The product of this sum = 24
"""

import numpy as np

n, m = map(int, input().split())
array = []
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

#print(np.sum(array, axis=0))
print(np.prod(array, axis=None))