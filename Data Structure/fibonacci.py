def matVacia(n):
	m = []
	for i in range(n):
		fila = []
		for j in range(n):
			fila.append(0)
		m.append(fila)
	return m
 
def mulMat(m1, m2, mod):
	n = len(m1)
	mr = matVacia(n)
	for i in range(n):
		for j in range(n):
			for k in range(n):
				mr[i][j]+=m1[i][k]*m2[k][j]
	for i in range(n):
		for j in range(n):
			mr[i][j]%=mod 
	return mr
 
def identidad(n):
	m = matVacia(n)
	for i in range(n):
		m[i][i] = 1
	return m
 
def expMat(m, n, mod):
	if(n == 0):
		return identidad(len(m))
	mr = expMat(m, n//2, mod)
	mr = mulMat(mr, mr, mod)
	if(n%2 == 1):
		mr = mulMat(m,mr, mod)
	return mr

def fib(n, mod):
	m = expMat([[0,1],[1,1]], n, mod)
	return m[1][1]%mod



print(fib(0, 100))
print(fib(1, 100))
print(fib(10, 10))
print(fib(3, 100))
print(fib(123456780, 10))
print(fib(3467, 9350))	
print(fib((1<<63), 10007))	

'''
0 1
1 1

f(0) = 0
f(1) = 1
f(2) = 1

1 1
1 2

f(1) = 1
f(2) = 1
f(3) = 2

3 5
5 8

f(4) = 3
f(5) = 5
f(6) = 8
'''








