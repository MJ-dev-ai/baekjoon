alpha = [0 for _ in range(26)]
string = input().lower()
for s in string:
    alpha[ord(s)-ord('a')] += 1
max_idx = 0
for idx in range(len(alpha)):
    if alpha[max_idx] < alpha[idx]:
        max_idx = idx
if alpha.count(alpha[max_idx]) > 1:
    print('?')
else:
    print(chr(max_idx + ord('a')).upper())