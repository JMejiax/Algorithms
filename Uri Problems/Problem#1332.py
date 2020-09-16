
def replace_(string, i, ch):
	new_ = ""
	
	for x in range(len(string)):
		if x == i:
			new_ += ch
		else:
			new_ += string[x]
	return new_
	
def clean_word(word):		
	letter = "one"	
	aux = ""
	
	if len(word) == 3:
	
		if 'o' in word and 'n' in word and 'e' in word:
			return 'one'
		if 't' in word and 'w' in word and 'o' in word:
			return 'two'
		
		for i in range(len(word)):
			aux = word
			for j in range(len(letter)):
				aux = replace_(aux, i, letter[j])	
				if aux == "one":			
					return "one"
		return "two"
		
	return "three"


resul = []
name_number = {
"one": 1,
"two": 2,
"three": 3,}

n = int(input())

for _ in range(n):
	word = input()

	word = clean_word(word)

	if word in name_number:
		resul.append(name_number[word])

print(*resul, sep="\n")







