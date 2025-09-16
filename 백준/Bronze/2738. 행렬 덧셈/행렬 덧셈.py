n, m = map(int, input().split())
array1, array2 = [], []
for i in range(n):
    row = list(map(int, input().split()))
    array1.append(row)
for i in range(n):
    row = list(map(int, input().split()))
    row = [x + y for x, y in zip(row, array1[i])]
    for j in row:
        print(j, end=" ")
    print()
    