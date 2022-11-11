from sys import stdin
input()
s, com= [], stdin.readlines()
cnt = 0
for x in com:
    c = x.split()
    if c[0] == "push":
        s.append(c[1])
    elif c[0] == 'pop':
        if len(s) > cnt:
            print(s[cnt])
            cnt += 1
        else: print(-1)
    elif c[0] == 'size':
        print(len(s)-cnt)
    elif c[0] == 'empty':
        if len(s) == cnt :
            print(1)
            cnt = 0
            s = []
        else: print(0)
    elif c[0] == 'front':
        if len(s) > cnt: print(s[cnt])
        else: print(-1)
    elif c[0] == 'back':
        if len(s) > cnt: print(s[-1])
        else: print(-1)

#------------------------------------------------------------
import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline())

for _ in range(N) :
    i = sys.stdin.readline().split()

    if i[0] == 'push' :
        queue.append(int(i[1]))
    
    elif i[0] == 'pop' :
        if not queue :
            print (-1)
        else :
            print(queue[0])
            queue.popleft()
    
    elif i[0] == 'size' :
        print(len(queue))
    
    elif i[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    
    elif i[0] == 'front' :
        if not queue:
            print(-1)
        else :
            print(queue[0])
    
    elif i[0] == 'back' :
        if not queue :
            print(-1)
        else :
            print(queue[-1])