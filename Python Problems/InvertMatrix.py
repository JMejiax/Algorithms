def invertImage(image):
	s = []
	m = []
	for i in range(len(image)-1, -1, -1):
		for j in range(len(image[0])-1, -1, -1):
			 s.append(str(image[i][j]))
		m.append(s)
		s = []
	print(*m, sep='\n')

invertImage([[7,2,3],[7,7,1]])
