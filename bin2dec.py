

def b2d(num):
    a = list(num)
    sum = 0
    for i in range(len(a)):
        bin_position = len(a) - i -1
        sum += (2**bin_position)*int(a[i])
    return sum

# binary_num = input() 
# dec = b2d(binary_num)
# print(dec)

def b2d_v1(num):
    pos = 0
    sum = 0
    while num > 0:
        # print('check',sum)
        quot = num//10
        rem = num%10
        sum += (2**pos)*rem
        num = quot
        pos +=1
    return sum

# binary_num = int(input())
# dec = b2d_v1(binary_num)
# print(dec)

def b2d_v2(num,pos=0):
    """
    (100)base2 = 1*2^2 + 0*2^1 + 0*2^0 = 4 base 10
    """
    print(f'check num = {num} pos = {pos}')
    quot = num//10
    rem = num%10
    return 0 if num == 0 else rem * (2**pos) + b2d_v2(quot,pos+1)
    

binary_num = int(input())
dec = b2d_v2(binary_num)
print(dec)
