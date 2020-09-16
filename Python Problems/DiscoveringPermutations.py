"""
In this problem you have to find the permutations using the first N English capital letters. Since there can be many permutations, you have to print the first K permutations.

input:
Input starts with an integer T (≤ 100), denoting the number of test cases.
Each case contains two integers N, K (1 ≤ N ≤ 26, 1 ≤ K ≤ 30).

output:
For each case, print the case number in a line. Then print the first K permutations that contain the first N English capital letters in alphabetical order. If there are less than K permutations then print all of them.

"""


from math import factorial
from itertools import permutations


def letras(c):
	abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	set_letras = []
	for i in range(c[0]):
		set_letras.append(abc[i])
	return set_letras


def perm(l, k):
	per = ""
	cont = 0
	f = factorial(len(l))
	if k < f:
		x = permutations(l)
		for permutacion in x:
			if cont <= k:
				for letra in permutacion:
					per += str(letra)
				print(str(per))
				per = ""
			else:
				break
			cont += 1
	else:
		#for comb in range(f):
		x = permutations(l)
		for permutacion in x:
			for letra in permutacion:
				per += str(letra)
			print(str(per))
			per = ""
		

t = int(input())

cases = []

for i in range(t):
	cases.append(list(map(int, input().split())))

for i in range(len(cases)):
	print("Case "+ str(i+1) + ":")
	perm(letras(cases[i]), cases[i][1])
	


