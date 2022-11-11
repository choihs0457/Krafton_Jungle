# input 입력 받기
n = int(input())
solution = list(map(int, input().split(' ')))

# 정렬하기
solution.sort()

# 이중포인터 설정
left = 0
right = n-1

answer = 2e+9+1 # 기준값
final = [] # 정답

# 투포인터 진행
while left < right:
    s_left = solution[left]
    s_right = solution[right]

    tot = s_left + s_right
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(tot) < answer:
        answer = abs(tot)
        final = [s_left, s_right]
	
    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if tot < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    else:
        right -= 1

print(final[0], final[1])

#---------------------------------------------------------------------------------------------------------------------------------

n = int(input())
arr = sorted(map(int, input().split()))  # 정렬된 용액들


def binary_search(s, target):
    global arr
    res = n
    start, end = s, n - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    return res


def solution():
    global arr
    v1, v2 = 0, 0
    best_sum = 10 ** 10
    for i in range(n):
        # 이분 탐색 수행: 현재 위치(i) 이후의 용액에서 탐색, 찾는 값은 (현재 용액 * -1)
        res = binary_search(i + 1, -arr[i])
        
        # 찾은 용액의 왼쪽 용액 확인
        if i + 1 <= res - 1 < n and abs(arr[i] + arr[res - 1]) < best_sum:
            best_sum = abs(arr[i] + arr[res - 1])
            v1, v2 = arr[i], arr[res - 1]

        # 찾은 용액 확인
        if i + 1 <= res < n and abs(arr[i] + arr[res]) < best_sum:
            best_sum = abs(arr[i] + arr[res])
            v1, v2 = arr[i], arr[res]
    
    print(v1, v2) # i 번째 용액을 확인할 때 i + 1번 용액부터 확인하기 때문에 항상 v1 <= v2 이다.


solution()