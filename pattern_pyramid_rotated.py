
rows = int(input())

# for i in range(rows):
#     print(" "*i + "*"*(rows-i))


for i in range(rows):
    print(" "*(rows-i) + "*"*i)