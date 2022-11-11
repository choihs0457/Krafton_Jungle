import sys
N, S = list(map(int, input().split()))
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
def func(sum, visited):
    global cnt
    if sum == S:
        cnt += 1
        return
    for i in range(N):
        if i not in visited and len(visited) < N:
            visited.append(i)
            func(sum + a[i], visited)
            visited.pop()
for i in range(N):
    visited = []
    visited.append(i)
    func(a[i], visited)
print(cnt)