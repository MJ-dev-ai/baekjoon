max = 0
max_idx = 0
for i in range(1,10):
    num = int(input())
    if max < num:
        max = num
        max_idx = i
print(max)
print(max_idx)