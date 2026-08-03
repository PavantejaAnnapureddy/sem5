
root = -1
for i in range(n):
    if parent[i] == -1:
        root = i
        break

root = parent.index(-1)  #
