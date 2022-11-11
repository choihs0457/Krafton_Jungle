def PN(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

test_case = int(input())
PN_list = []
cnt = 0

for a in range(test_case):
    test = int(input())
    for x in range(test-1, 1, -1):
        if PN(x) == True:
            PN_list.append(x)
    start = len(PN_list)//2
    for y in range(start, 0, -1):
        if cnt == 1:
            break
        if PN_list[y] * 2 == test:
            print(PN_list[y],PN_list[y])
            cnt = 1
        for z in range(start,len(PN_list)):
            if cnt == 1:
                break
            if PN_list[y] + PN_list[z] == test:
                print(PN_list[z], PN_list[y])
                cnt = 1
