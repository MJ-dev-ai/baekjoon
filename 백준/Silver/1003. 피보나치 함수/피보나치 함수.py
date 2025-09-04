def fibonacci_count(n):
    dp = [(1,0), (0,1)] # 0일 때 (1,0), 1일 때 (0,1)
    for i in range(2, n+1):
        c0 = dp[i-1][0] + dp[i-2][0] # dp[i] = dp[i-1] + dp[i-2]
        c1 = dp[i-1][1] + dp[i-2][1]
        dp.append((c0,c1))
    return dp[n]

import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    c0, c1 = fibonacci_count(n)
    print(c0, c1)