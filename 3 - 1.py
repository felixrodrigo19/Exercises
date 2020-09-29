numero = int(input('Entre com o número: '))

for x in range(numero):
	if x*(x+1)/2 == numero:
		is_triangular = True
	else:
	    is_triangular = False

print(is_triangular)
