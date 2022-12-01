import sys

input = sys.stdin.readline

Ex = input().rstrip().split("-")
Ans_list = []

for E in Ex:
    sum = 0
    E_minus = E.split("+")
    for E_object in E_minus:
        sum += int(E_object)
    Ans_list.append(sum)
ans = Ans_list[0]

for pointer in range(1, len(Ans_list)):
    ans -= Ans_list[pointer]

print(ans)
