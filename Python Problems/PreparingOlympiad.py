"""
You have n problems. You have estimated the difficulty of the i-th one as integer c i. Now you want to prepare a problemset for a contest, using some of the problems you've made.

A problemset for the contest must consist of at least two problems. You think that the total difficulty of the problems of the contest must be at least l and at most r. Also, you think that the difference between difficulties of the easiest and the hardest of the chosen problems must be at least x.

Find the number of ways to choose a problemset for the contest.

input:
The first line contains four integers n, l, r, x (1 ≤ n ≤ 15, 1 ≤ l ≤ r ≤ 109, 1 ≤ x ≤ 106) — the number of problems you have, the minimum and maximum value of total difficulty of the problemset and the minimum difference in difficulty between the hardest problem in the pack and the easiest one, respectively.
The second line contains n integers c 1, c 2, ..., c n (1 ≤ c i ≤ 106) — the difficulty of each problem.

output:
Print the number of ways to choose a suitable problemset for the contest.

"""


def suma_o_resta(a, b):
	return (a & (1<<b))

def diferencia(s1, d):
	if s1:
		s1.sort()
		#print(*s1, sep=" - ")
		if s1[-1] - s1[0] >= d:
			#print(str(s1[-1]) + " - " + str(s1[0]) + " = " + str(s1[-1] - s1[0]))
			return s1
		else:
			return diferencia(s1.remove(s1[-1]), d)	
	return s1

def no_sets(v, n, l, r, d):
	s = []
	cont = 0
	for x in range(1<<n):
		for i in range(n):
			#print("(" + str(x) + ", " + str(i) + ")")
			if suma_o_resta(x, i) > 0:
				#print(str(suma_o_resta(x, i)))
				s.append(v[i])
		s = diferencia(s, d)
		if s:
			if sum(s) >= l and sum(s) <= r:
				cont += 1
		s = []
	return cont;
	

n, l, r, x = map(int, input().split())

v = list(map(int, input().split()))

print(str(no_sets(v, n, l, r, x)))





