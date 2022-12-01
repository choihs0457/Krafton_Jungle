import sys

input = sys.stdin.readline

N = int(input())
List = []
DP = [[0] * N for _ in range(N)]

for _ in range(N):
    List.append(list(map(int, input().split())))

DP[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(DP[N - 1][N - 1])
        else:
            if i + List[i][j] < N:
                DP[i + List[i][j]][j] += DP[i][j]
            if j + List[i][j] < N:
                DP[i][j + List[i][j]] += DP[i][j]
