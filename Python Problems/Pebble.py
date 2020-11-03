# Link Problema: https://vjudge.net/problem/UVA-10651

def TEST(msk, i):
	return (msk & (1<<i))

def SET(msk, i):
	return (msk | (1<<i))

def CLEAR(msk, i):
	return (msk	 & (~(1<<i)))

memo = [-1]*((1<<12))
def min_bolas(msk):
	if memo[msk] != -1:
		return memo[msk]
	hay_jugadas = 0
	mini = 13	
	for i in range(10):
		if TEST(msk, i) and TEST(msk, i+1) and (not TEST(msk, i+2)):
			hay_jugadas += 1
			n_msk = CLEAR(msk, i)
			n_msk = CLEAR(n_msk, i+1)
			n_msk = SET(n_msk, i+2)
			mini = min(mini, min_bolas(n_msk))
	for i in range(2, 12):
		if TEST(msk, i) and TEST(msk, i-1) and (not TEST(msk, i-2)):
			hay_jugadas += 1
			n_msk = CLEAR(msk, i)
			n_msk = CLEAR(n_msk, i-1)
			n_msk = SET(n_msk, i-2)
			mini = min(mini, min_bolas(n_msk))
	if not hay_jugadas:
		memo[msk] = cant_bits(msk)
		return memo[msk]
	memo[msk] = mini
	return memo[msk]

		
def cant_bits(msk):
	cant = 0
	for i in range(12):
		if TEST(msk, i):
			cant += 1
	return cant			

def table_to_msk(table):
	msk = ''
	for ch in table:
		if ch == '-':
			msk += '0'
		else:
			msk += '1'
	return int(msk, 2)


cases = int(input())
tables = []

for _ in range(cases):
	table = input()
	tables.append(table_to_msk(table))

for msk in tables:
	print(min_bolas(msk))



'''
#if TEST(4, 2) and TEST(2, 1):
msk = 384

print(TEST(msk, 7))
print(TEST(msk, 8))	
print(TEST(msk, 9))
 
msk = CLEAR(msk, 7)
msk = CLEAR(msk, 8)
print(msk)

msk = SET(msk, 9)
print(msk)
'''


# i = 3
#index	11	  10    9   8    7   6   5  4  3 2 1 0
#		------------------------------------------
#  		2048  1024  512 256  128 64  32 16 8 4 2 1
#  		1     1     1   1    1   1   1  1  1 1 1 1 
#  		------------------------------------------
#msk	0     0     0   1    1   0   0  0  0 0 0 0
#i = 7	0     0     0   0    1   0   0  0  0 0 0 0
#~i= 7	0     0     0   0    0   1   1  1  1 1 1 1
#	    ------------------------------------------
#clear7	0     0     0   0    0   0   0  0  0 0 0 0
#set 7	0     0     0   0    1   0   0  0  0 0 0 0








