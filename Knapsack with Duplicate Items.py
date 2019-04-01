# Given weights and values related to n items and the maximum capacity allowed for these items. What is the maximum value we can achieve if we can pick any weights any number of times for a total allowed weight of W?

# Input:
# The first line of input contains an integer denoting the number of test cases. Then T test cases follow . Each test case contains two integers N and W denoting the number of items and the total allowed weight. In the next two lines are space separated values of the array denoting values of the items (val[]) and their weights (wt[]) respectively.

# Output:
# For each test case, in a new line, print the  maximum value which we can achieve if we can pick any weights any number of times for a bag of size W.

# Constraints:
# 1 <= T <= 100
# 1 <= N, W <= 103
# 1 <= wt[], val[] <= 100

# Example:
# Input:
# 2
# 2 3
# 1 1
# 2 1 
# 4 8
# 1 4 5 7
# 1 3 4 5
# Output:
# 3
# 11

# ** For More Input/Output Examples Use 'Expected Output' option **
# https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items/0

def solve(weights, values,w): 
    n = len(weights)
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(w+1):
            if weights[i-1]>j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(values[i-1]+dp[i][j-weights[i-1]], dp[i-1][j])
    print(dp[-1][-1])
    
for _ in range(int(input())):
    [n, w] = [int(_) for _ in input().strip().split()]
    values = [int(_) for _ in input().strip().split()]
    weights = [int(_) for _ in input().strip().split()]
    solve(weights, values, w)
            