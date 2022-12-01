import sys

input = sys.stdin.readline

Coin_count, Key_point = map(int, input().split())
Coin_list = []
count = 0
for _ in range(Coin_count):
    Coin_list.append(int(input()))

for coin in range(1, Coin_count + 1):
    count += Key_point // Coin_list[-coin]
    Key_point %= Coin_list[-coin]
    if Key_point == 0:
        break

print(count)
