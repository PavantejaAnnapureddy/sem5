import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i, val in enumerate(p):
        pos[val] = i
    
    adj = [[] for _ in range(n + 1)]
    indeg = [0] * (n + 1)
    
    for i in range(1, n):
        if pos[i] < pos[i + 1]:
            adj[i].append(i + 1)
            indeg[i + 1] += 1
        else:
            adj[i + 1].append(i)
            indeg[i] += 1
    
    heap = [i for i in range(1, n + 1) if indeg[i] == 0]
    heapq.heapify(heap)
    
    result = []
    while heap:
        u = heapq.heappop(heap)
        result.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)
    
    print(*result)# cook your dish here
