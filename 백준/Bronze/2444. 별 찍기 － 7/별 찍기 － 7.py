n = int(input())
for i in range(1, n + 1):
    result = " " * (n - i) + "*" * (2 * i - 1)
    print(result)
for j in range(1, n):
    result = " " * j + "*" * (2*n - 2*j - 1)
    print(result)