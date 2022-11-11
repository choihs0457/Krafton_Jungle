import sys
input = sys.stdin.readline

N, M = map(int, input().split())
li = list(map(int, input().split()))
min = 1
max = max(li)


while min <= max :
    cut = 0
    mid = (min + max)//2

    for x in li:
        if x > mid:
            cut += x-mid
    if cut < M:
        max = mid -1
    else:
        min = mid +1

print(max)