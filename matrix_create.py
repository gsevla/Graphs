matrix = []


def matrix_create(l, c):
    global matrix
    print('Put the matrix values line by line: ')
    for i in range(l):
        line = []
        for j in range(c):
            line.append(int(input('[{}][{}]: '.format(i, j))))
        matrix.append(line)
    print()
    print('Matrix:')
    for k in range(len(matrix)):
        print(matrix[k])


if __name__ =='__main__':
    matrix_create(2,2)
