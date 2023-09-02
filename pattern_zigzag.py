
"""
  *   *
 * * * *
*   *   *
"""

num_star = int(input())

# for i in range(3):
#     for j in range(num_star):
#         print("*",end = '') if ((i+j) % 4 == 2 and i%2 == 0) else print(' ',end='')
#     print('\n')

for i in range(3):
    for j in range(num_star):
        if i in [0,2]:
            if ((i+j) % 4 == 2):
                print("*",end='')  
            else: 
                print(' ',end='')
        if i == 1:
            if ((i+j) % 2 == 0):
                print("*",end='')  
            else: 
                print(' ',end='')
    print('\n')
