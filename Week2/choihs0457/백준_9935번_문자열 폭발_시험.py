import sys
input = sys.stdin.readline

def sol():
    cnt = 0
    tmp.clear()
    for x in range(1, len(boom)+1):
        if stack[-1] == boom[-x]:
            tmp.append(stack.pop())
            cnt += 1
        else:
            break
    if cnt != len(boom):
        for _ in range(len(tmp)):
            stack.append(tmp.pop())
            print(stack)
    else:
        return        
        
N = input()
K = input()

N_sol = list(N)
N_sol.pop()
boom = list(K)
boom.pop()
stack = []
tmp = []

for i in range(len(N_sol)):
    stack.append(N_sol[i])
    if stack[-1] == boom[-1]:
        sol()

if stack:
    print(''.join(stack))
else:
    print("FRULA")