
"""
100 // 8 = 12, 100 % 8 = 4
12 // 8 = 1, 12 % 8 = 4
1 // 8 = 0, 1 % 8 = 1
"""

def divide_by_8(num):
    """
    n - num
    Time - O(logn) -> T(n) = T(n/2) + O(1)
    Space - O(logn) -> Height of Recursion Stack = log(n)
    """
    # print('check',num)
    if num > 7:
        divide_by_8(num // 8)
    print(num % 8,end = '')

decimal = int(input())
divide_by_8(decimal)