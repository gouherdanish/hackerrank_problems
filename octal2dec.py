def o2d(num,pos=0):
    """
    (144)base8 = 1*8^2 + 4*8^1 + 4*8^0 = (100) base 10
    """
    print(f'check num = {num} pos = {pos}')
    quot = num//10
    rem = num%10
    return 0 if num == 0 else rem * (8**pos) + o2d(quot,pos+1)
    

print(o2d(int(input())))