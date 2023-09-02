
rows = int(input())

for i in range(rows):
    # end = 1
    for j in range(i+1):
        start = 1 if (i+j) %2 == 0 else 0
        print(start,end=' ') if j < i else print(start,end='\n')
    # print('\n')