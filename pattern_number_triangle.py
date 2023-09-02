
rows = int(input())

for i in range(rows):
    print(" "*(rows-i-1) + " ".join([str(x) for x in range(1,i+2)]))