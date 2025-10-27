num, b = map(int, input().split())
result = ""
while num >= b:
    remain = num % b
    if remain < 10:
        result = str(chr(remain + ord('0'))) + result
    else:
        result = str(chr(remain - 10 + ord('A'))) + result
    num = num // b

if num < 10: result = str(chr(num + ord('0'))) + result
else:
    result = str(chr(num - 10 + ord('A'))) + result

print(result)