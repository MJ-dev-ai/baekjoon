t = int(input())
for _ in range(t):
    string = input()
    if len(string) == 1:
        print(string[0]*2)
    else:
        print(string[0], string[-1],sep="")