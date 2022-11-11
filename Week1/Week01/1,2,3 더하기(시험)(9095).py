import sys
from itertools import combinations_with_replacement
from itertools import product

a = int(sys.stdin.readline())
cnt = 0
for _ in range(a):
    b = int(sys.stdin.readline())
    for x in range(1,b+1):
        res = list(product([1,2,3],repeat = x))
        for i in res:
            if sum(i) == b:
                cnt += 1
    print(cnt)
    cnt = 0