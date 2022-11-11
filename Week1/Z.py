def z(x, y, z):
    if x == 0:
        return 0
    return 2*int(y%2)+int(z%2)+4*z(x-1,(y/2),(z/2))
    
a, b, c = map(int, input().split())
z(a, b, c)
