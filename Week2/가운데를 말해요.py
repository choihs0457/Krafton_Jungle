import sys
import heapq

input = sys.stdin.readline

N = int(input())
downvalue = []
upvalue = []

def save(value: int):
    if len(downvalue) == len(upvalue):
        heapq.heappush(downvalue, (-value, value))
    else:
        heapq.heappush(upvalue, value)
    
    if upvalue and downvalue[0][1] > upvalue[0]:
        down = downvalue[0][1]
        up = upvalue[0]
        heapq.heappop(downvalue)
        heapq.heappop(upvalue)
        heapq.heappush(downvalue, (-up, up))
        heapq.heappush(upvalue, (down))

for i in range(N):
    heap = int(input())
    save(heap)
    print(downvalue[0][1])