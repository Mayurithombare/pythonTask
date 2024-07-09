
def pyramid(rows):
    for i in range(rows):
        print()
        for j in range(i+1):
            print('*',end='')

pyramid(5)