
def check_pythagorean(a,b,c):
    return c**2 == a**2 + b**2

x,y,z = sorted([int(x) for x in input().split(' ')])
print(check_pythagorean(x,y,z))