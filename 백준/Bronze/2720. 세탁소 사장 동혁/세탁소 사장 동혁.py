t = int(input())
coins = (25, 10, 5, 1)
for _ in range(t):
    money = int(input())
    for coin in coins:
        print(money // coin, end=' ')
        money = money % coin
    print()