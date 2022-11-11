import sys

def sol(n):
    global cnt
    x = n//10
    y = n%10
    z = x+y
    N = y*10+z%10
    cnt += 1
    if a == N:
        print(cnt)
        return
    sol(N)

a = int(sys.stdin.readline())
cnt = 0

sol(a)