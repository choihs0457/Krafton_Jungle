n = int(input())
in_list = list(map(int ,input().split()))
visited = [False]*n
answer = 0
def sol(li):
  global answer
  if len(li) == n:
    total = 0
    for i in range(n-1):
      total += abs(li[i]- li[i+1])
    answer = max(answer, total)
    return

  for i in range(n):
    if not visited[i]:
      visited[i] = True
      li.append(in_list[i])
      sol(li)
      visited[i] = False
      li.pop()

sol([])
print(answer)

#------------------------------------------------------------------------------------------------------------

import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

cases = list(permutations(A))

answer = 0
for case in cases:
    mid_sum = 0
    for i in range(N - 1):
        mid_sum += abs(case[i] - case[i + 1])
    answer = max(mid_sum, answer)

print(answer)