import sys
from collections import deque

input = sys.stdin.readline

def topology_sort():
    res = []
    q = deque()
    
    for value in range(1,Num+1):
        if Student_indgree[value] == 0:
            q.append(value)
    
    while q:
        now = q.popleft()
        res.append(now)
        for S in Student_Match_list[now]:
            Student_indgree[S] -= 1
            if Student_indgree[S] == 0:
                q.append(S)

    return print(*res)


Num, Match = map(int, input().split())
Student_Match_list = [[] for _ in range(Num+1)]
Student_indgree = [0 for _ in range(Num+1)]


for _ in range(Match):
    Student_first, Student_second = map(int, input().split())
    Student_Match_list[Student_first].append(Student_second)
    Student_indgree[Student_second] += 1

topology_sort()
