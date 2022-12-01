import sys

input = sys.stdin.readline

Case = int(input())

for _ in range(Case):
    Applicant = int(input())
    Grade_list = []
    for _ in range(Applicant):
        Doc_score, Interview_score = map(int, input().split())
        Grade_list.append([Doc_score, Interview_score])

    Grade_list.sort()

    Ans = 1
    Cut_line = Grade_list[0][1]
    for pointer in range(1, Applicant):
        if Grade_list[pointer][1] < Cut_line:
            Ans += 1
            Cut_line = Grade_list[pointer][1]

    print(Ans)
