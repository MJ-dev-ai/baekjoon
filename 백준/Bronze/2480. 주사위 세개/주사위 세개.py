dices = input().split()
dices = [int(dice) for dice in dices]
if dices[0]==dices[1]==dices[2]:
    print(10000+dices[0]*1000)
elif dices[0]==dices[1] or dices[0]==dices[2]:
    print(1000+dices[0]*100)
elif dices[1]==dices[2]:
    print(1000+dices[1]*100)
else:
    print(max(dices)*100)