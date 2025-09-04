x = int(input())
n = int(input())
total = 0
for _ in range(n):
    inputs = input().split()
    a, b = int(inputs[0]), int(inputs[1])
    total += a*b
print("Yes" if total == x else "No")