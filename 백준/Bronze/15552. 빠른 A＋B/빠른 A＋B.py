import sys

t = int(input())
for _ in range(t):
    inputs = sys.stdin.readline().rstrip().split()
    a, b = int(inputs[0]), int(inputs[1])
    print(a+b)