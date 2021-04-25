print('Set Number 1 and 2:')
n1 = int(input('1º> '))
if(n1 == empty()):
	print('Erro')
n2 = int(input('2º> '))

op = 0
while op != 6:
	print('''[ 1 ] Addition
[ 2 ] Subtraction
[ 3 ] Multiplication
[ 4 ] Division
[ 5 ] Cleaner
[ 6 ] Exit''')
	print('*' * 40)
	op = int(input('Set Options'))
	print('*' * 40)
	if op == 1:
		print(n1 + n2)
	elif op == 2:
		result = n1 - n2
		print('{}-{} = {}'.format(n1, n2, result))