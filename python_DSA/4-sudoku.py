correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


# Define a function check_sudoku() here:
def check_sudoku(puzzle):
    l = len(puzzle)
    for row in puzzle:
        check = list(range(1, l+1))
        for i in row:
            if i not in check:
                return False
            check.remove(i)
    for i in range(l):
        check = list(range(1, l+1))
        for row in puzzle:
            if row[i] not in check:
                return False
            check.remove(row[i])
    return True


print(check_sudoku(incorrect))
print(check_sudoku(correct))
print(check_sudoku(incorrect2))
print(check_sudoku(incorrect3))
print(check_sudoku(incorrect4))
print(check_sudoku(incorrect5))
