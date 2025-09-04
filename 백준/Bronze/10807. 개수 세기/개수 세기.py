import sys

line = sys.stdin.readline().rstrip()
n = int(line)
arr = sys.stdin.readline().rstrip().split()
arr = [int(e) for e in arr]
line = sys.stdin.readline().rstrip()
v = int(line)
if v not in arr: print(0)
else:
    arr.sort()
    start = arr.index(v)
    stop = start
    while True:
        if stop == len(arr) - 1: break
        if arr[start] != arr[stop + 1]: break
        else: stop += 1
    print(stop - start + 1)