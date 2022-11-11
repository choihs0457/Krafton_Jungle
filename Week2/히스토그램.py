import sys
input = sys.stdin.readline
def hst_area(h, l, r):
    global cnt
    cnt = 0
    if l == r:
        return h[l]
    else: # l < r :
        mid = (l + r) // 2
        maxLeft = hst_area(h, l, mid)
        maxRight = hst_area(h, mid + 1, r)
        pl, pr = mid, mid + 1
        width = 2
        height = min(h[pl], h[pr])
        maxMid = width * height
        while pl <= 0 and pr <= r :
            cnt += 1
            width += 1
            height_l = h[pl - 1] if l < pl else 0
            height_r = h[pr + 1] if pr < r else 0
            if height_l > height_r:
                height = min(height, height_l)
                pl -= 1
            else:
                height = min(height, height_r)
                pr += 1
            maxMid = max(maxMid, width * height)
        return max(maxLeft, maxMid, maxRight)
while True:
    h = list(map(int, input().strip().split()))
    n = h.pop(0)
    if n == 0:
        break
    print(hst_area(h, 0, n - 1), cnt)