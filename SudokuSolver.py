matrix = [
  ["5", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


def isValid(currVal, bit):
  return (currVal & (1 << bit)) == 0

def allFilled(matrix):
  for row in matrix:
    if '.' in row:
      return False
  return True
  
def isCellClear(matrix, ii, jj, k):
  sset = set()
  rStart = ii // 3 * 3
  cStart = jj // 3 * 3
  for i in range(rStart, rStart + 3):
    for j in range(cStart, cStart + 3):
      if matrix[i][j] != '.':
        if matrix[i][j] in sset:
          return False
        sset.add(matrix[i][j])
  return True

def helper(matrix, rows, cols):
  if allFilled(matrix):
    return True
  
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == '.':
        for k in range(1, 10):
          if isValid(rows[i], k) and isValid(cols[j], k) and isCellClear(matrix, i, j, k):
            rows[i] |= (1 << k)
            cols[j] |= (1 << k)
            matrix[i][j] = k
            if helper(matrix, rows, cols):
              return True
            rows[i] ^= (1 << k)
            cols[j] ^= (1 << k)
            matrix[i][j] = '.'
        
        return False
  
  return False

def solve(matrix):
  rows = [0 for _ in range(9)]
  cols = [0 for _ in range(9)]
  
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] != '.':
        matrix[i][j] = int(matrix[i][j])
        rows[i] |= (1 << matrix[i][j])
        cols[j] |= (1 << matrix[i][j])
  
  return helper(matrix, rows, cols)
  

if solve(matrix):
  for row in matrix:
    print(row)
else:
  print('Not solvable')
