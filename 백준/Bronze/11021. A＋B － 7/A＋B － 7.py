import sys

t = int(input())
for case in range(t):
    inputs = sys.stdin.readline().rstrip().split()
    a, b = int(inputs[0]), int(inputs[1])
    print(f"Case #{case+1}: {a+b}")