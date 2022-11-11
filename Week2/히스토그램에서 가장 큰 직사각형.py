N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))


def solve(s, e):
    if s == e:
        return 0
    if s+1 == e:
        return arr[s]

    mid = (s + e) // 2
    result = max(solve(s, mid), solve(mid, e))

    w = 1
    h = arr[mid]
    l = mid
    r = mid

    while r-l+1 < e-s:
        p = min(h, arr[l-1]) if l > s else -1
        q = min(h, arr[r+1]) if r < e-1 else -1
        
        if p >= q:
            h = p
            l -= 1
        else:
            h = q
            r += 1
        w += 1
        result = max(result, w*h)

    return result


print(solve(0, N))

#---------------------------------------------------------------------------------

# import sys
# input = sys.stdin.readline

# def sol(L: list, H: int, T: int):
#     global sum
#     global start
#     global ans
#     search(L, H, T)
#     for i in range(T,len(L)):
#         if L[i] == H:
#             search(L, H, i)

# def search(L: list, H: int, T: int):
#     global sum
#     global start
#     global ans
#     sum = H
#     while T != len(L)-1 and H <= L[T+1]:
#         sum += H
#         if ans < sum:
#             ans = sum
#         start = T
#         T = T+1

# while True:
#     li = list(map(int, input().split()))
#     save = []
#     global ans
#     ans = 0
#     if li[0] == 0:
#         break
#     del li[0]
#     for i in range(len(li)):
#         if li[i] in save:
#             continue
#         save.append(li[i])

#         sum = li[i]
#         sol(li,li[i],i)
#     print(ans)
#---------------------------------------------------------------------------------

# def plus_search(x: list, y: int):
#     global sum
#     now = x[y]
#     while y != len(x)-1 and now <= x[y+1]:
#         sum += now
#         y = y+1

# def minus_search(x: list, y: int):
#     global sum
#     now = x[y]
#     while y != 0 and now <= x[y-1]:
#         sum += now
#         y = y-1

# def sol(x: list, y: int):
#     global ans
#     global sum
#     plus_search(x, y)
#     minus_search(x,y)
#     if ans < sum:
#         ans = sum

# while True:
#     li = list(map(int, input().split()))
#     if li[0] == 0:
#         break
#     del li[0]
#     ans = len(li)*min(li)
#     for i in range(len(li)):
#         now = li[i]
#         x = i
#         while now <= li[x-1]:
#             x = x-1
#             if x == 0:
#                 break
#         if x != 0:
#             sum = li[i]
#             sol(li,i)
#     print(ans)
