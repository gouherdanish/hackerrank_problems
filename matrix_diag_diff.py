def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sum_diag1 = 0
    sum_diag2 = 0
    for row in range(n):
        sum_diag1 += arr[row][row]
        sum_diag2 += arr[row][n - row - 1]
    return abs(sum_diag1-sum_diag2)