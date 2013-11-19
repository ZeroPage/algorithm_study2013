#Trailblaze
def is_p_bigger_than_q(p, q):

    queue = [q]
    chk = [False] * (n + 1)

    while len(queue) > 0:
        s = queue[len(queue) - 1]
        queue.pop()
        if chk[s]:
            continue
        chk[s] = True
        for w in graph[s]:
            if not chk[w]:
                queue.append(w)

    return chk[p]

n, m = map(int, raw_input().split())
graph = []
for _ in range(n + 2):
    graph.append([])
for i in range(m):
    x, y = map(int, raw_input().split())
    graph[y].append(x)

p, q = map(int, raw_input().split())

flagP = is_p_bigger_than_q(p, q)
flagQ = is_p_bigger_than_q(q, p)

if not flagP and not flagQ:
    print 'unknown'
elif flagP:
    print 'yes'
elif flagQ:
    print 'no'



