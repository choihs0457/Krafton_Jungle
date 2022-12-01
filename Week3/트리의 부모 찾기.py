import sys
from collections import deque
input = sys.stdin.readline

Node = int(input())
Node_list = [[] for _ in range(Node+1)]
P_list = [0 for _ in range(Node+1)]
visited = [False for _ in range(Node+1)]

for _ in range(Node-1):
    P, S = map(int, input().split())
    Node_list[P].append(S)
    Node_list[S].append(P)

def P_search(list: list, now: int, visited: list):
    visited[now] = True
    stack = deque([now])    
    while stack:
        N = stack.pop()
        for i in list[N]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                P_list[i] = N

P_search(Node_list, 1, visited)
for i in range(2,Node+1):
        print(P_list[i])