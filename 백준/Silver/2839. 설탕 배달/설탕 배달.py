n = int(input())
n3 = 0
n5 = n // 5
while(1):
    if (n5 == 0):
        break
    remain = n - (n5 * 5)
    if (remain % 3 == 0):
        n3 = remain // 3
        break
    n5 -= 1
    
remain = n - (n5 * 5)
n3 = remain // 3
if (remain % 3 == 0):
    print(n3 + n5)
else:
    print(-1)