import sys

input = sys.stdin.readline


def sol():
    sol_list = [0] * (Goal + 1)
    sol_list[0] = 1
    for coin in Coin_type:
        for i in range(Goal + 1):
            if i >= coin:
                sol_list[i] += sol_list[i - coin]
    return sol_list[Goal]


T_count = int(input())
while T_count != 0:
    T_count -= 1
    Coin_count = int(input())
    Coin_type = list(map(int, input().split()))
    Goal = int(input())
    print(sol())
