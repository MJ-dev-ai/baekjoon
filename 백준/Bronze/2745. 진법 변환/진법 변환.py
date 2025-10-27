n, b = input().split()
b = int(b)
result = 0
for chr in n:
    result *= b
    if ord('0') <= ord(chr) <= ord('9'): result += int(chr)
    else: result += ord(chr) - ord('A') + 10
print(result)