import sys

input = sys.stdin.readline

New = int(input())
ans_list = [0] * 1000001
ans_list[1] = 1
ans_list[2] = 2
for i in range(3, New + 1):
    ans_list[i] = (ans_list[i - 2] + ans_list[i - 1]) % 15746
print(ans_list[New])
