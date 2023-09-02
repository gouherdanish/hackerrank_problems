
rows = int(input())
print(rows)

num = 1
for i in range(rows):
    start = num
    end = num + i + 1
    print(' '.join([str(x) for x in range(start,end)]))
    num = end
    

# for i in range(1,rows+1):
#     for j in range(num):
#         print(num,end = ' ')
#         num+=1
    # print('\n')