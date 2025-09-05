n = int(input())
arr = input().split()
arr = [int(num) for num in arr]
arr.sort()
print(arr[0],arr[-1])