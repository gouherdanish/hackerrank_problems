
"""
7 // 2 = 3, 7 % 2 = 1
3 // 2 = 1, 3 % 2 = 1
1 // 2 = 0, 1 % 2 = 1
"""
def divide_by_2(num,a=[]):
    quot = num // 2
    rem = num % 2
    a.insert(0,str(rem))
    if quot < 1:
        return a
    else:
        return divide_by_2(quot)

# decimal = int(input())
# a = divide_by_2(decimal)
# print("".join(a))

def divide_by_2_v1(num):
    """
    n - num
    Time - O(logn) -> T(n) = T(n/2) + O(1)
    Space - O(logn) -> Height of Recursion Stack = log(n)
    """
    print('check',num)
    if num > 1:
        divide_by_2_v1(num // 2)
    print(num % 2,end = '')

decimal = int(input())
divide_by_2_v1(decimal)