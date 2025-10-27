n = int(input())
dot_line = 2
for i in range(n):
    dot_line = dot_line * 2 - 1
print(dot_line ** 2)