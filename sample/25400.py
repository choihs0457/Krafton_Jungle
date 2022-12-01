import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
j = 0
cnt = 0


while True:
    if j == len(arr):
        break
    for i, val in enumerate(arr[j:]):
        if i + j + 1 != val:
            del arr[i + j]
            cnt += 1
            j += i
            break

print(cnt)
