#Trailblaze

n, w = map(int, raw_input().split(' '))
horizon = [None] * n
for i in range(n):
    x, y = map(int, raw_input().split(' '))
    horizon[i] = [x, y]


stack = [0]
horizon.append([w+1, 0])
horizon.insert(0, [0, 0])
building  = 0
for i in range(n+2):
    while stack[len(stack) - 1] > horizon[i][1]:
        building = building + 1
        stack.pop()

    if stack[len(stack) - 1] < horizon[i][1]:
        stack.append(horizon[i][1])

print building


#Trailblaze
a = input()
fact = 1
for i in range(1, a + 1):
    fact = fact * i
print fact