#Trailblaze

n = input()
beadPattern = raw_input() * 3
p1 = n
p2 = 2*n
ans = 0

for i in range(p1, p2):

    bw1 = rw1 = bw2 = rw2 = 0
    for j in range(i-1, i-n, -1):
        if beadPattern[j] == 'r' :
            break
        else :
            bw1 = bw1 + 1
    for j in range(i-1, i-n, -1):
        if beadPattern[j] == 'b' :
            break
        else :
            rw1 = rw1 + 1
    for j in range(i, i + n):
        if beadPattern[j] == 'r' :
            break
        else :
            bw2 = bw2 + 1
    for j in range(i, i + n):
        if beadPattern[j] == 'b' :
            break
        else :
            rw2 = rw2 + 1

    temp = max(rw1, bw1) + max(rw2, bw2)
    if temp > n:
        temp = n;
    ans = max(temp, ans)


print ans
