import sys

a = int(input())
b = []
for _ in range(a):
    b.append(int(sys.stdin.readline()))

print(*sorted(b), sep = '\n')