"""
Petr has just bought a new car. He's just arrived at the most known Petersburg's petrol station to refuel it when he suddenly discovered that the petrol tank is secured with a combination lock! The lock has a scale of 360 degrees and a pointer which initially points at zero:

Petr called his car dealer, who instructed him to rotate the lock's wheel exactly n times. The i-th rotation should be ai degrees, either clockwise or counterclockwise, and after all n rotations the pointer should again point at zero.

This confused Petr a little bit as he isn't sure which rotations should be done clockwise and which should be done counterclockwise. As there are many possible ways of rotating the lock, help him and find out whether there exists at least one, such that after all n rotations the pointer will point at zero again.

input:
The first line contains one integer n (1≤n≤15) — the number of rotations.

Each of the following n lines contains one integer ai (1≤ai≤180) — the angle of the i-th rotation in degrees.

output:
If it is possible to do all the rotations so that the pointer will point at zero after all of them are performed, print a single word "YES". Otherwise, print "NO". Petr will probably buy a new car in this case.

"""


def suma_o_resta(a, b):
	return (a & (1<<b))

def has_lock(v, n):
	suma = 0
	for x in range(1<<n):
		for i in range(n):
			if suma_o_resta(x, i) > 0:
				suma += v[i]
			else:
				suma += -1*v[i]
		if suma%360 == 0:
			return "YES"
		suma = 0
	return "NO"

rotations = int(input())

v = []

for i in range(rotations):
	v.append(int(input()))

print(has_lock(v, rotations))


"""
       128 64 32 16 8 4 2 1
1    =  0  0  0  0  0 0 0 1
--------------------------
1<<0 =  0  0  0  0  0 0 0 1
1<<1 =  0  0  0  0  0 0 1 0
1<<2 =  0  0  0  0  0 1 0 0


comb = 0
suma_o_resta(0, 0) = 0 & (1<<0) = F = 0 suma -= 10
suma_o_resta(0, 1) = 0 & (1<<1) = F = 0 suma -= 20
suma_o_resta(0, 2) = 0 & (1<<2) = F = 0 suma -= 30
				 						Total = -60
comb = 1
suma_o_resta(1, 0) = 1 & (1<<0) = V = 1 suma += 10
suma_o_resta(1, 1) = 1 & (1<<1) = F = 0 suma -= 20
suma_o_resta(1, 2) = 1 & (1<<2) = F = 0 suma -= 30
				 						Total = -40
comb = 2
suma_o_resta(2, 0) = 2 & (1<<0) = F = 0 suma -= 10
suma_o_resta(2, 1) = 2 & (1<<1) = V = 2 suma += 20
suma_o_resta(2, 2) = 2 & (1<<2) = F = 0 suma -= 30
				 						Total = -20
comb = 3
suma_o_resta(3, 0) = 3 & (1<<0) = V = 1 suma += 10
suma_o_resta(3, 1) = 3 & (1<<1) = V = 2 suma += 20
suma_o_resta(3, 2) = 3 & (1<<2) = F = 0 suma -= 30
				 						Total = 0
comb = 4
suma_o_resta(4, 0) = 4 & (1<<0) = F = 0 suma -= 10
suma_o_resta(4, 1) = 4 & (1<<1) = F = 0 suma -= 20
suma_o_resta(4, 2) = 4 & (1<<2) = V = 4 suma += 30
								    	Total = 0
comb = 5
suma_o_resta(5, 0) = 5 & (1<<0) = V = 1 suma += 10
suma_o_resta(5, 1) = 5 & (1<<1) = F = 0 suma -= 20
suma_o_resta(5, 2) = 5 & (1<<2) = F = 4 suma += 30
				 						Total = 20
comb = 6
suma_o_resta(6, 0) = 6 & (1<<0) = F = 0 suma -= 10
suma_o_resta(6, 1) = 6 & (1<<1) = V = 2 suma += 20
suma_o_resta(6, 2) = 6 & (1<<2) = V = 4 suma += 30
				 						Total = 40
comb = 7
suma_o_resta(7, 0) = 7 & (1<<0) = V = 1 suma += 10
suma_o_resta(7, 1) = 7 & (1<<1) = V = 2 suma += 20
suma_o_resta(7, 2) = 7 & (1<<2) = V = 4 suma += 30
				 						Total = 60
"""
