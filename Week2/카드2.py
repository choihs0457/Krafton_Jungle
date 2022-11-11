# import sys
# input = sys.stdin.readline

# N = int(input())
# li = [i for i in range(1,N+1)]
# while len(li) != 1:
#     if len(li)%2 == 0:
#         for x in range(0,len(li)//2):
#             del li[x]
#     else:
#         for x in range(0,(len(li)//2)+1):
#             del li[x]

# print(li[0])
#----------------------------------------

import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque()

for i in range(1,n+1):
    card.append(i)

while len(card) != 1:
    card.popleft()
    card.append(card.popleft())
print(card[0])