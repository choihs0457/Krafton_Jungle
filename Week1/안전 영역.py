import sys

def check(z, x, y):
    if li[x][y] > z:
        check_li[x][y] = True
        return  True
    else:
        check_li[x][y] = False
        return  False

def plag(z, x,y):
    if check(z, x, y):
        plag_li[x][y] = 1
        return  True
    else:
        plag_li[x][y] = 1
        return  False

def sol(z, x, y) :
    global cnt
    if x > w or y > w or x < 0 or y < 0 :
        return

    if plag_li[x][y] == 1:
        sol(z, x, y+1)
    
    if plag_li[x][y] == 0:
        if plag(z, x, y):
            sol(z, x, y+1)
            sol(z, x, y-1)
            sol(z, x+1, y)
            sol(z, x-1, y)
            cnt += 1
            return

w = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(w)]
check_li = [list(True for _ in range(w)for _ in range(w))]
plag_li = [list(0 for _ in range(w))for _ in range(w)]

print(plag_li[1][1])

cnt = 0
dep = max(map(max, li))
ans = 0

for E in range(dep+1):
    sol(E, 0, 0)
    cnt = max(ans, cnt)
    ans = cnt