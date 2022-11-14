import sys
from collections import deque
input = sys.stdin.readline

def BFS(start: int):
    queue = deque([start])
    checked[start] = True
    distance[start] = 0
    ans = []
    while queue:
        s = queue.popleft()
        for i in edges[s]:
            if not checked[i]:
                queue.append(i)
                checked[i] = True
                distance[i] = distance[s] + 1
                if distance[i] == lenth:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i, end='\n')


node, edge, lenth, first = map(int, input().split())
edges = [[] for _ in range(node+1)]
checked = [False for _ in range(node+1)]
distance = [0 for _ in range(node+1)]

for _ in range(edge):
    start, end = map(int, input().split())
    edges[start].append(end)

BFS(first)