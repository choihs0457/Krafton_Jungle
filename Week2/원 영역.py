import sys
from collections import deque


def sol(L)



input = sys.stdin.readline
li = []
N = int(input())
for _ in range(N):
    L, R = map(int, input().split())
    L_spot = L-R
    R_spot = L+R
    li.append([L_spot,R_spot])
li.sort(key = lambda x: (x[0], -x[1]))
print(li)