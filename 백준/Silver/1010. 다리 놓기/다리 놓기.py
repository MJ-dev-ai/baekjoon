def combination(a, b):
    u, l = 1, 1
    for i in range(b):
        u *= a-i
        l *= i+1
    return u//l
import sys

t = int(input())
for _ in range(t):
    inputs = sys.stdin.readline().split()
    a, b = int(inputs[0]), int(inputs[1])
    print(combination(b, a))