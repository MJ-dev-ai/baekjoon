n, m = input().split()
n, m = int(n), int(m)
baskets = [i for i in range(n+1)]
for _ in range(m):
    i, j = input().split()
    i, j = int(i), int(j)
    baskets[i:j+1] = baskets [j:i-1:-1]
for idx in range(1,n+1):
    print(baskets[idx],end=" ")