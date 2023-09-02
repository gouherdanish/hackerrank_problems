conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
                    4: '4', 5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B',
                    12: 'C', 13: 'D', 14: 'E', 15: 'F'}

conv_dict = {v:k for k,v in conversion_table.items()}

def h2d(num):
    """
    (100)base2 = 1*2^2 + 0*2^1 + 0*2^0 = 4 base 10
    """
    a = list(num)
    print(a)
    sum = 0
    for i in range(len(a)):
        pos = len(a) - i -1
        print(i, pos)
        sum += (16**pos)*int(conv_dict[a[i]])
    return sum

hex_num = input() 
dec = h2d(hex_num)
print(dec)