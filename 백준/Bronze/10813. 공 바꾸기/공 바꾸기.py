n, m = input().split()
n, m = int(n), int(m)
result = [i for i in range(n+1)]
for _ in range(m):
    i, j = input().split()
    i, j = int(i), int(j)
    temp = result[i]
    result[i] = result[j]
    result[j] = temp
for idx in range(1,n+1):
    print(result[idx],end=" ")