import sys

input = sys.stdin.readline

Sequence_len = int(input())
Sequence = list(map(int, input().split()))

DP = [0 for _ in range(Sequence_len)]
for pointer_one in range(Sequence_len):
    for pointer_two in range(pointer_one):
        if (
            Sequence[pointer_one] > Sequence[pointer_two]
            and DP[pointer_one] < DP[pointer_two]
        ):
            DP[pointer_one] = DP[pointer_two]
    DP[pointer_one] += 1
print(max(DP))
