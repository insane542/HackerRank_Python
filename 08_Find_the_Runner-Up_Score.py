"""
Task:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
Store them in a list and find the score of the runner-up.

Input Format:
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
* 2<=n<=10
* -100<=A[i]<=100

Output Format:
Print the runner-up score.

Sample Input 0:
5
2 3 6 6 5

Sample Output 0:
5

Explanation 0:
Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    #I did mnually sorting in descending or just use arr.sort(reverse=True)
    for i in range(n): 
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    max_value = arr[0]
    runner_up = None
    
    for i in range(1, n):
        if arr[i] != max_value:
            runner_up = arr[i]
            break
    print(runner_up)