import sys

def sol(ali: list, a : int):
    global ans
    if len(ali) == w-1:
        ali.append(li[a][0])
        ans = min(ans,  sum(ali))
        ali.pop()
        return

    for x in range(a, w):
        for y in range(1, w):
            if li[x][y] == 0:
                continue
            if not visited[y]: 
                visited[y] = True
                ali.append(li[x][y])
                sol(ali, y)
                visited[y] = False
                ali.pop()

w = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(w)]
visited = [False]*w
ans = 99999999999999

sol([], 0)
print(ans)

#------------------------------------------------------------------------------------------------------------

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
visit = [0] * n
m = 1e9

def dfs(depth, start, cost):
    global m
    if depth == n-1 and l[start][0] != 0:
        m = min(m, cost+l[start][0])
        return
    for i in range(n):
        if not visit[i] and l[start][i] != 0:
            visit[i] = 1
            dfs(depth+1, i, cost+l[start][i])
            visit[i] = 0
visit[0] = 1
dfs(0, 0, 0)
print(m)
