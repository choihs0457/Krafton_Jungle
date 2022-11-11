import sys
from itertools import combinations


a, b = map(int, input().split())
c = list(map(int, sys.stdin.readline().split()))
cnt = 0

for x in range(1,len(c)+1):
    res = list(combinations(c, x))
    for i in res:
        print(i, sum(i))
        if sum(i) == b:
            cnt += 1
print(cnt)