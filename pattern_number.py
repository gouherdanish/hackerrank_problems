
rows = int(input())

for i in range(rows):
    num = rows - i
    print(' '.join([str(x) for x in range(1,num+1)]))