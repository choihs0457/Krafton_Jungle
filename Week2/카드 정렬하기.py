import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

def card_sum(card_list: list):
    sum = 0
    ans = 0
    while len(card_list) != 1:        
        sum = card_list[0]
        heapq.heappop(card_list)
        sum += card_list[0]
        ans += sum
        heapq.heappop(card_list)
        heapq.heappush(card_list, sum)
    print(ans)

for i in range(N):
    heapq.heappush(heap,int(input()))

card_sum(heap)