import sys
from collections import deque


k = int(input())
food_times = list(map(int, input().split()))


ans = deque()
for i in range(len(food_times)):
    ans.append(i + 1, food_times[i] - 1)
    # print(ans)
    k = k - 1

for _ in range(k):
    if not ans:
        break
    print(ans)
    a, b = ans.popleft
    if b - 1 == 0:
        continue
    else:
        ans.append([a, b - 1])

if ans:
    a, b = ans.popleft
    print(a)
else:
    print(-1)
