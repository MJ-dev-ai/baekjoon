n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0
for i in range(len(arr)):
    res += (n - i) * arr[i]
print(res)