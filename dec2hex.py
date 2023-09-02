
"""
100 // 16 = 6, 100 % 16 = 4
6 // 16 = 0, 6 % 16 = 6

30 // 16 = 1, 30 % 16 = 14 => E
1 // 16 = 0, 1 % 16 = 1 => 1
"""

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def divide_by_16(num):
    """
    n - num
    Time - O(logn) -> T(n) = T(n/2) + O(1)
    Space - O(logn) -> Height of Recursion Stack = log(n)
    """
    print('check',num)
    if num > 15:
        divide_by_16(num // 16)
    print(conversion_table[num % 16],end = '')

decimal = int(input())
divide_by_16(decimal)