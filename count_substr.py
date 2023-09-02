def count_substring(string, sub_string):
    start = 0
    end = len(string)
    num = 0
    found = True
    while(found and start <= end):
        idx = string[start:].find(sub_string)
        if idx == -1:
            found = False
            return num
        else:
            idx = idx + start
            num += 1
            start = idx + 1

    return num

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)