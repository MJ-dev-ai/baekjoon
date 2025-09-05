arr = [i for i in range(1,31)]
for _ in range(28):
    submit = int(input())
    arr[submit - 1] = 0
res = [i for i in arr if i != 0]
print(res[0],res[1],sep='\n')