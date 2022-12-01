import sys

input = sys.stdin.readline

New = int(input())
F = 0
S = 1
cnt = 1

if New == 0:
    print(0)
elif New == 1:
    print(1)
else:
    while cnt != New:
        F, S = S, F + S
        cnt += 1
    print(S)
