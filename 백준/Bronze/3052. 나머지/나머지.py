s = set()
for _ in range(10):
    num = int(input())
    s.add(num % 42)
print(len(s))