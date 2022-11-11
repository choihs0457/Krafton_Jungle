import sys

input = sys.stdin.readline

N = int(input())
Quard_list = []
for i in range(N):
    Quard = input()
    print(Quard)
    Quard_list.append(list(Quard))
    print(Quard_list)


# def solution(x, y, N) :
#   color = paper[x][y]
#   for i in range(x, x+N) :
#     for j in range(y, y+N) :
#       if color != paper[i][j] :
#         solution(x, y, N//2)
#         solution(x, y+N//2, N//2)
#         solution(x+N//2, y, N//2)
#         solution(x+N//2, y+N//2, N//2)
#         return
#   if color == 0 :
#     result.append(0)
#   else :
#     result.append(1)