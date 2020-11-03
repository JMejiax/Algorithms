# A list to memoize the fibonacci numbers
memo = [-1]*10000
# A function to calculates de the fibonacci number of n
def fib(n):
	if n == 1:
		return 1
	if n == 0:
		return 0
	if memo[n] != -1:
		return memo[n]
	memo[n] = fib(n-1) + fib(n-2)
	return memo[n]

# A list to memoize the number of recursive calls that a number will get
calls = [0]*10000
# A function to calculate the number of recursive calls of a number n.
def fib_calls(n):
	if n == 1 or n == 0:
		return 1
	if calls[n] != 0:
		return calls[n]
	calls[n] = 1 + fib_calls(n-1) + fib_calls(n-2)
	return calls[n]


tests = int(input())
resul = []

for _ in range(tests):
	
	n = int(input())
	f = fib(n)
	c = fib_calls(n)-1
	
	r = 'fib('+str(n)+') = ' + str(c) + ' calls = ' + str(f)
	resul.append(r)
	memo = [-1]*10000
	calls = [0]*10000
	
print(*resul, sep='\n')

