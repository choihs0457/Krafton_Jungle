import sys
input = sys.stdin.readline

N = int(input())
H_list = []

for _ in range(N):
    new_H = int(input())
    H_list.append(new_H)

    if min(H_list) < new_H:
        for x in range(len(H_list)-2,-1,-1):
            if H_list[x] <= new_H:
                del H_list[x]
                print(H_list)

print(len(H_list))
#-----------------------------------------------------------------------

import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    stack.append(int(input()))

last = stack[-1]
count = 1

for i in reversed(range(N)):
    if stack[i] > last:
        count += 1
        last = stack[i]

print(count)