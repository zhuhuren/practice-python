#This function adds a number to each item in a nested sequence
def plusNum(L, num):
	for i in range(len(L)):
		if not isinstance( L[i], list):
			L[i] += 10
		else: plusNum(L[i], num)

##>>> L = [[3, 5, 2, [3, 46, [2, 5, [3, 6, 3, 3], 3, 6, 2, [3, 5, 7]], 4, 6, [3, 4, 67, [3, 4]]], 3, 6], [3, 7, 2]]
##>>> plusNum(L, 10)
##>>> L
##[[13, 15, 12, [13, 56, [12, 15, [13, 16, 13, 13], 13, 16, 12, [13, 15, 17]], 14, 16, [13, 14, 77, [13, 14]]], 13, 16], [13, 17, 12]]
##>>> 
