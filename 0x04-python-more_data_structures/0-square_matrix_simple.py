def square_matrix_simple(matrix=[]):

    rows = len(matrix)
    cols = len(matrix[0])

    squared_matrix = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            squared_matrix[i][j] = matrix[i][j] ** 2

    for row in squared_matrix:
        return squared_matrix
