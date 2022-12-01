import sys

input = sys.stdin.readline

Rock_count, Fake_rock_count = map(int, input().split())

Fake_rock = set()
for _ in range(Fake_rock_count):
    Fake_rock.add(int(input()))

dp = [[10001] * (int((2 * Rock_count) ** 0.5) + 2) for _ in range(Rock_count + 1)]

dp[1][0] = 0
for i in range(2, Rock_count + 1):
    if i in Fake_rock:
        continue
    for v in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][v] = min(dp[i - v][v - 1], dp[i - v][v], dp[i - v][v + 1]) + 1


ans = min(dp[Rock_count])
if ans == 10001:
    print(-1)
else:
    print(ans)
