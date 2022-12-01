import sys

input = sys.stdin.readline

First_str = input().strip()

Second_str = input().strip()

h = len(First_str)
w = len(Second_str)
check_list = [[0] * (w + 1) for _ in range(h + 1)]

for h in range(1, h + 1):
    for w in range(1, w + 1):
        if First_str[h - 1] == Second_str[w - 1]:
            check_list[h][w] = check_list[h - 1][w - 1] + 1
        else:
            check_list[h][w] = max(check_list[h][w - 1], check_list[h - 1][w])
print(check_list[-1][-1])
