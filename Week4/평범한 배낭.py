import sys

input = sys.stdin.readline


def sol():
    for i in range(1, Article_count + 1):
        for j in range(1, resistance_weight + 1):
            weight = Article_list[i][0]
            value = Article_list[i][1]

            if j < weight:
                Sol_list[i][j] = Sol_list[i - 1][j]
            else:
                Sol_list[i][j] = max(
                    value + Sol_list[i - 1][j - weight], Sol_list[i - 1][j]
                )

    return Sol_list[Article_count][resistance_weight]


Article_count, resistance_weight = map(int, input().split())
Article_list = [[0, 0]]
Sol_list = [[0 for _ in range(resistance_weight + 1)] for _ in range(Article_count + 1)]

for _ in range(Article_count):
    Article_weight, Article_value = map(int, input().split())
    Article_list.append([Article_weight, Article_value])

print(sol())
