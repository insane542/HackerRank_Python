"""
Problem:
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications.
* Mat size must be N x M. (N is an odd natural number, and M is times N.)
* The design should have "WELCOME" written in the center.
* The design pattern should only use |,. and - characters.

Sample Design:
Size: 7 x 21
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

Size: 11 x 33
---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------

Input Format:
A single line containing the space separated values of N and M.

Constraints:
* 5 < N < 101
* 15 < M < 303

Output Format:
Output the design pattern.

Sample Input 0:
9 27

Sample Output 0:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_design_pattern(n, m):
    # Top half
    for i in range(1, n, 2):
        pattern = ('.|.' * i).center(m, '-')
        print(pattern)
    
    # Middle line
    print('WELCOME'.center(m, '-'))
    
    # Bottom half
    for i in range(n-2, 0, -2):
        pattern = ('.|.' * i).center(m, '-')
        print(pattern)

if __name__ == "__main__":
    n, m = map(int, input().split())
    print_design_pattern(n, m)