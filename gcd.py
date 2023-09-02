import functools

"""
Input
n = 2 m = 3
a = [2 4]
b = [16 32 96]

2 and 4 divide evenly into 4, 8, 12 and 16 => mid_arr
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all
"""

def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

def getTotalX(a, b):
    # Write your code here
    lcm = functools.reduce(lambda x, y: compute_lcm(x,y), a)
    print(lcm)
    mid_arr = [lcm*i for i in range(1,b[0]+1) if lcm*i <= b[0]]
    print(mid_arr)
    count = 0
    b_factor_arr = []
    for elm in mid_arr:
        print(elm)
        flag = False
        for target in b:
            if target % elm !=0:
                flag = False
                break
            else:
                flag = True
        if flag:
            count+=1
    return count