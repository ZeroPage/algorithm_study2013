#Skywave

inputData = raw_input().split()
target = int(inputData[1])
length = len(inputData[0])
result = 0


data = inputData[0]

for i in range(length):
    if i != 0:
        result += int(data[:i]) * (10 ** (length - i - 1))
        if target == 0:
            result -= 10 ** (length - i - 1)
    elif target == 0:
        continue

    if i != length - 1:
        if int(data[i]) == target or target == 0:
            result += int(data[-(length - 1 - i):]) + 1
        elif int(data[i]) > target:
            result += 10 ** (length - i - 1)
    else:
        if int(data[i]) >= target:
            result += 1

print "%d" %result