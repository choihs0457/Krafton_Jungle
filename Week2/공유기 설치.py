import sys
input = sys.stdin.readline

N, C = map(int, input().split())
li = []
for _ in range(N):
    li.append(int(input()))

li.sort()

L = li[0]
R = li[-1]
start = 1

while start <= R:
    mid = (start+R)//2
    cnt = 1
    now = li[0]

    for x in range(1,N):
        if li[x] >= now + mid:
            cnt += 1
            now = li[x]  
    if cnt >= C:
        start = mid + 1
        ans = mid
    else:
        R = mid - 1

print(ans)