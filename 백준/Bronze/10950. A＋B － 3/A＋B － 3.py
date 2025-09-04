repeat_count = int(input())
for _ in range(repeat_count):
    inputs = input().split()
    a, b = int(inputs[0]), int(inputs[1])
    print(a+b)