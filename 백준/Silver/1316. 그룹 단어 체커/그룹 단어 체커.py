def is_groupword(word):
    set_alpha = {word[0]}
    prev = word[0]
    for s in word[1:]:
        if s == prev: continue
        else:
            if s in set_alpha:
                return 0
            else:
                set_alpha.add(s)
                prev = s
    return 1
n = int(input())
result = 0
for _ in range(n):
    string = input()
    result += is_groupword(string)
print(result)