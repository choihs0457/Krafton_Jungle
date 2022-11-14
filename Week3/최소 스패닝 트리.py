# import sys

# v, e = map(int, input().split())
# # 부모 테이블 초기화
# parent = [0] * (v+1)
# for i in range(1, v+1):
#     parent[i] = i

# # find 연산
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # union 연산
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 간선 정보 담을 리스트와 최소 신장 트리 계산 변수 정의
# edges = []
# total_cost = 0

# # 간선 정보 주어지고 비용을 기준으로 정렬
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     edges.append((cost, a, b))

# # 간선 정보 비용 기준으로 오름차순 정렬
# edges.sort()

# # 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
# for i in range(e):
#     cost, a, b = edges[i]
#     # find 연산 후, 부모노드 다르면 사이클 발생 X으므로 union 연산 수행 -> 최소 신장 트리에 포함!
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         total_cost += cost

# print(total_cost)

import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))
 
Elist.sort(key=lambda x: x[2])
 
 
def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]
 
 
answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)