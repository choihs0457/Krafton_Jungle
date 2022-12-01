import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())
DP = [[0] * N for _ in range(M)]
cnt = 0
List = []

for _ in range(M):
    List.append(list(map(int, input().split())))


def search(i: int, j: int):
    DP[0][0] = 1
    for i in range(M):
        for j in range(N):
            if DP[i][j] > 0:
                if j + 1 < N and List[i][j] > List[i][j + 1]:
                    DP[i][j + 1] += DP[i][j]
        for j in range(-1, -N - 1, -1):
            if DP[i][j] > 0:
                if j - 1 > -N - 1 and List[i][j] > List[i][j - 1]:
                    DP[i][j - 1] += DP[i][j]
        for j in range(N):
            if DP[i][j] > 0:
                if i + 1 < M and List[i][j] > List[i + 1][j]:
                    DP[i + 1][j] += DP[i][j]


search(0, 0)
print(DP[M - 1][N - 1])
