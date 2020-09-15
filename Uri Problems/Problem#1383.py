def is_valid(sudoku):
	seen = set()
	
	for i in range(len(sudoku)):
		for j in range(len(sudoku)):
		
			number = str(sudoku[i][j])
			
			p1 = number + " en la fila " + str(i) 
			p2 = number + " en la columna " + str(j) 
			
			cuadricula = str(i//3) + ", " + str(j//3)
			p3 = number + " en la cuadricula " + cuadricula 
			

			if p1 in seen or p2 in seen or p3 in seen:
				return False
			else:
				seen.add(p1)
				seen.add(p2)
				seen.add(p3)
	return True

n = int(input())

sudoku = []
resul = []

for test in range(n):
	sudoku = []
	for f in range(9):
		fila = list(map(int, input().split()))
		sudoku.append(fila)
	
	if is_valid(sudoku):
		resul.append("Instancia " + str(test+1) + "\nSIM\n")
	else:
		resul.append("Instancia " + str(test+1) + "\nNAO\n")

print(*resul, sep="\n")



