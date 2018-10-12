def trianglePasc(intdepth):
    matrix = []
    for i in range(intdepth):
        matrix.append([])
        for j in range(intdepth):
            if(i + j <= intdepth - 1):
                matrix[i].append(-1)


    for i in range(intdepth):
        matrix[0][i] = 1
        matrix[i][0] = 1

    for i in range(intdepth):
        for j in range(intdepth):
            if( i + j <= intdepth - 1):
                if(matrix[i][j] == -1):
                   matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix


inta = int(input())
matrix = trianglePasc(inta)
for i in range (inta):
    print(matrix[i])

