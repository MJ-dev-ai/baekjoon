import sys
from collections import deque

t = int(input())
for _ in range(t):
    inputs = sys.stdin.readline().strip().split()
    n, k = int(inputs[0]), int(inputs[1])
    d_array = sys.stdin.readline().strip().split()
    d_array = [int(d) for d in d_array]
    graph = [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for _ in range(k):
        inputs = sys.stdin.readline().strip().split()
        x, y = int(inputs[0]), int(inputs[1])
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = d_array[i-1]
    for i in range(1, n+1):
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            dp[next] = max(dp[next],dp[now]+d_array[next-1])
            if indegree[next] == 0:
                q.append(next)
    print(dp[w])