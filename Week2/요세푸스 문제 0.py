import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

YSPS = deque()
YSPS_ans = []

for i in range(1, N+1):
    YSPS.append(i)

while len(YSPS) != 0:
    for _ in range(K-1):
        YSPS.append(YSPS.popleft())
    YSPS_ans.append(YSPS.popleft())
print("<",end='')
print(*YSPS_ans,sep = ', ',end='')
print(">")