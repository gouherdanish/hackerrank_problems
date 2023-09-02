
rows = int(input())

for i in range(rows):
    print("*"*(i+1) + " "*2*(rows-i-1) + "*"*(i+1))

for i in range(rows,0,-1):
    print("*"*(i) + " "*2*(rows-i) + "*"*(i))