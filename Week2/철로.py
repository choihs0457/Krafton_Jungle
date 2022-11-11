import sys
import heapq

input = sys.stdin.readline
         
N = int(input())
temp_list = []
ans_list = []
ans = 0

for _ in range(N):
    home, company = map(int, input().split())

    if home > company:
        home, company = company, home
        temp_list.append([home, company,company - home])
    else:
        temp_list.append([home, company,company - home])

L = int(input())

temp_list.sort(key=lambda x:x[1])

for x in temp_list:
    if x[2] > L:
        continue
    if len(ans_list) == 0:
        heapq.heappush(ans_list, x)
        continue
    else:
        while ans_list[0][0] < x[1] - L:
            heapq.heappop(ans_list)
        heapq.heappush(ans_list, x)
    ans = max(len(ans_list), ans)
print(ans)
