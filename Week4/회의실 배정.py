import sys

input = sys.stdin.readline

Meeting_count = int(input())
Timetable = []


for _ in range(Meeting_count):
    S, E = map(int, input().split())
    Timetable.append([S, E])

Timetable.sort(key=lambda x: (x[1], x[0]))

ans = 1
end_time = Timetable[0][1]
for pointer in range(1, Meeting_count):
    if Timetable[pointer][0] >= end_time:
        ans += 1
        end_time = Timetable[pointer][1]

print(ans)
