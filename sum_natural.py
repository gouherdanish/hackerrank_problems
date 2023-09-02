
def sum_n(n):
    return 1 if n == 1 else n + sum_n(n-1)

print(sum_n(int(input())))