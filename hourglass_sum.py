"""
Find the sum of the elements in a hourglass matrix

a b c
  d
e f g

"""

def hourglassSum(arr):
    # Write your code here
    max_sum = float('-inf')
    for i in range(4):
        for j in range(4):
            # print(f'i={i}')
            subarr = [arr[i][j:(j+3)],arr[i+1][j:(j+3)],arr[i+2][j:(j+3)]]
            # print(subarr)
            subarr[1][0] = 0
            subarr[1][2] = 0
            print(subarr)
            curr_sum = sum(map(sum,subarr))
            if curr_sum > max_sum:
                max_sum = curr_sum
            # print(max_sum)
    return max_sum