# cook your dish here
def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        adj = [[] for _ in range(n+1)]
        for _ in range(n-1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        
        deg = [len(adj[i]) for i in range(n+1)]
        
        leaves = [i for i in range(1, n+1) if deg[i] == 1]
        L = len(leaves)
        
        leaf_neighbors = {}
        for u in leaves:
            v = adj[u][0]
            leaf_neighbors[v] = leaf_neighbors.get(v, 0) + 1
        
        sum_choose = sum(k*(k-1)//2 for k in leaf_neighbors.values())
        
        D2 = sum(1 for i in range(1, n+1) if deg[i] == 2)
        D2_leaf = sum(1 for i in range(1, n+1) if deg[i] == 2 
                      and any(deg[neighbor] == 1 for neighbor in adj[i]))
        
        total = n * (n-1) * (n-2) // 6
        invalid = L * (n - 2) - sum_choose + D2 - D2_leaf
        
        print(total - invalid)

solve()