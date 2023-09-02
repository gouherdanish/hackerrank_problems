
def factorial(n):
    return 1 if n in [0,1] else n * factorial(n-1)

def ncr(n,r):
    return int(factorial(n) / (factorial(r) *  factorial(n-r)))

def pascal_triangle(n):
    for i in range(1,n+1):
        if i < 2:
            print(1)
            continue
        for j in range(i+1):
            # print("check",i,j)
            print(ncr(i,j),end = ' ') if j!= i else print(ncr(i,j),end = '\n')
        # print('\n')

if __name__=='__main__':
    # print(int(ncr(5,1)))
    pascal_triangle(int(input()))