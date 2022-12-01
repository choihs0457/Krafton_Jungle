import sys

input = sys.stdin.readline

Socket_count, Use_count = map(int, input().split())
Socket = [0 for _ in range(Socket_count)]

Use = list(map(int, input().split()))
cnt = 0
Target = 0
Now = 0

for P, value in enumerate(Use):
    if value in Socket:
        continue
    elif 0 in Socket:
        Socket[Socket.index(0)] = value
    else:
        for Check_P, check_value in enumerate(Socket):
            if check_value not in Use[P:]:
                Target = Check_P
                Socket[Check_P] = value
                break
            elif Use[P:].index(check_value) > Now:
                Target = Check_P
                Now = Use[P:].index(check_value)
        cnt += 1
        Now = 0
        Socket[Target] = value

print(cnt)
