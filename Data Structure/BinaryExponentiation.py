# Explaining: https://youtu.be/L-Wzglnm4dM

# Measure time: python3 -m timeit -s 'from BinaryExponentiation import power' 'power(10,18)'

# Calculate the power of a number
def power(a, b):
	result = 1
	while b: # while b > 0
		if b&1: # is odd?
			result *= a
		a *= a
		b //= 2
	return result

# Calculate the power of a number and calculate modulo of m	
def power_mod(a, b, m):
	result = 1
	while b > 0:
		if b%2==1:
			result = (result*a)%m
		a = (a*a)%m
		b //= 2
	return result

# Calculate fibonacci - Not as fast as Matrix Exponentiation
def fib(n):
	a = 0
	b = 1
	for i in range(2, n+1):
		new_a = 0 * a + 1 * b
		new_b = 1 * a + 1 * b
		
		a = new_a
		b = new_b
	return b

print(power(2,61))
print((1<<63))
#print(power_mod(100000000000000000000000000, 100000000000000000000000000, 100029))
