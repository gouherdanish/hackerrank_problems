
rows = int(input())
columns = int(input())

for i in range(rows):
    if i in [0,rows-1]:
        print(f"*"*columns)
    else:
        print("*" + " "*(columns-2) + "*")