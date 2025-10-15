inputs = []
for _ in range(5):
    inputs.append(input())

result = ""
for i in range(15):
    for j in range(5):
        if i < len(inputs[j]):
            result += inputs[j][i]
print(result)