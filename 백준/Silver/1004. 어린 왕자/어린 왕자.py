import sys, math
t = int(input())
for _ in range(t):
    inputs = sys.stdin.readline().strip().split()
    inputs = [int(element) for element in inputs]
    x1,y1,x2,y2=inputs
    n = int(input())
    if x1==x2 and y1==y2:
        print(0)
        for _ in range(n):
            _ = sys.stdin.readline()
    else:
        count = 0
        for _ in range(n):
            inputs = sys.stdin.readline().strip().split()
            inputs = [int(element) for element in inputs]
            cx,cy,r = inputs
            d1 = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)
            d2 = math.sqrt((x2 - cx)**2 + (y2 - cy)**2)
            if (d1 < r and r < d2) or (d2 < r and r < d1):
                count += 1
        print(count)