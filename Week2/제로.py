import sys

N = int(sys.stdin.readline())
li = []

for _ in range(N):
    commend = int(sys.stdin.readline())
    if commend == 0:
        li.pop()
    else:
        li.append(commend)

print(sum(li))