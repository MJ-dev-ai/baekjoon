import sys
from collections import deque

t = int(input())
for _ in range(t):
    inputs = sys.stdin.readline().strip().split()
    # 건물 갯수 N과 규칙의 갯수 K
    n, k = int(inputs[0]), int(inputs[1])
    # 각 건물을 지을 때 드는 시간을 가지는 d_array
    d_array = sys.stdin.readline().strip().split()
    d_array = [int(d) for d in d_array]
    # 조건을 저장할 graph, 진입차수 indegree
    # 최종으로 건물을 지을 때 드는 시간을 저장할 dp
    graph = [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    # 그래프 불러오기
    for _ in range(k):
        inputs = sys.stdin.readline().strip().split()
        x, y = int(inputs[0]), int(inputs[1])
        graph[x].append(y)
        indegree[y] += 1
    # 짓고자 하는 건물 W
    w = int(input())
    # 빈 queue에 진입차수가 0인 건물을 전부 넣기
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            # 진입차수가 0인 건물의 dp값은 해당 건물의 건설 시간
            dp[i] = d_array[i-1]
    # 위상정렬
    for i in range(1, n+1):
        now = q.popleft()
        # 왼쪽에서 가져온 건물을 조건으로 가지는 모든 건물에 대해 수행
        for next in graph[now]:
            indegree[next] -= 1
            # 전 건물의 dp값+next건물의 건설시간중 큰 값을 dp에 저장
            dp[next] = max(dp[next],dp[now]+d_array[next-1])
            if indegree[next] == 0:
                q.append(next)
    print(dp[w])