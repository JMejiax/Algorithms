# Calculate the minimum cost of convert a square to a magic square
# https://www.hackerrank.com/challenges/magic-square-forming/problem

def m_to_a(s):
    arr_s = []
    for i in range(len(s)):
        for j in range(len(s[0])):
            arr_s.append(s[i][j])
    return arr_s

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    arr_s = m_to_a(s)
    squares = [
        [8,1,6,3,5,7,4,9,2],
        [6,1,8,7,5,3,2,9,4],
        [4,9,2,3,5,7,8,1,6],
        [2,9,4,7,5,3,6,1,8],
        [8,3,4,1,5,9,6,7,2],
        [4,3,8,9,5,1,2,7,6],
        [6,7,2,1,5,9,8,3,4],
        [2,7,6,9,5,1,4,3,8]
    ]

    min_cost = 100000
    suma = 0
    for square in squares:
        for i, grid in enumerate(square):
            suma += abs(arr_s[i] - grid)
        min_cost = min(min_cost, suma)
        suma = 0
    return min_cost

s = [[4,9,2],
	 [3,5,7],
	 [8,1,5]]

print(formingMagicSquare(s))
