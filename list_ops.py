if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command = input().split(' ')
        command_str = command[0].lower()
        if command_str == 'insert':
            idx = int(command[1])
            elm = int(command[2])
            arr.insert(idx,elm)
        elif command_str == 'print':
            print(arr)
        elif command_str == 'remove':
            elm = int(command[1])
            arr.remove(elm)
        elif command_str == 'append':
            elm = int(command[1])
            arr.append(elm)
        elif command_str == 'sort':
            arr.sort()
        elif command_str == 'pop':
            arr.pop()
        elif command_str == 'reverse':
            arr.reverse()
        else:
            print('Invalid command')
        ``