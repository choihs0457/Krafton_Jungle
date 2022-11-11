def hanoi(x, s, m, e):
    if x == 1:
        print(s,e)
        return

    hanoi(x-1, s, e, m)
    print(s,e) 
    hanoi(x-1, m, s, e)

a = int(input())
print(2**a-1)
if a<=20: 
    hanoi(a, 1, 2, 3)
