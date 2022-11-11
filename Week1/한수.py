a = int(input())
cnt = 0
if a < 100 :
    print(a)

else:
    for x in range(100, a+1):
        b = x // 100
        c = (x%100) // 10
        d = (x%100)%10
        if b-c == c-d :
            cnt += 1
    print(99+cnt)
