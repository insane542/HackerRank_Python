"""
Task:
Given an integer, n, perform the following conditional actions:
* If n is odd, print Weird
* If n is even and in the inclusive range of 2 to 5, print Not Weird
* If n is even and in the inclusive range of 6 to 20, print Weird
* If n is even and greater than 20, print Not Weird

Input Format:
A single line containing a positive integer, n.

Constraints:
* 1<=n<=100

Output Format:
Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0:                                                             Sample Input 1:
3                                                                           24

Sample Output 0:                                                            Sample Output 1:
Weird                                                                       Not Weird

Explanation 0:                                                              Explanation 1:
n = 3                                                                       n = 24
n is odd and odd numbers are weird, so print Weird.                         n > 20 and n is even, so it is not weird
"""

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")