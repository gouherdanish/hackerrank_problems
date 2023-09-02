
rows = int(input())

for i in range(1,rows+1):
    print(" "*(rows-i) + "".join([str(x) for x in range(i,0,-1)]) + "".join([str(x) for x in range(2,i+1)]))