#!/usr/bin/python3
'__autor__'=='__Ivanoel__'

def fatorial(n):

	print("Calculando o fatorial de %d" %n)
	
	if n == 0 or n == 1:
		print("Fatorial de %d = 1" % n)
		return 1
	else:
		fat = n*fatorial(n-1)
		print("fatorial de %d = %d"%(n,fat))
	return fat
fatorial(5)