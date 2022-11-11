import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a = input()
    b = list(a)
    sum = 0
    for i in b:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')