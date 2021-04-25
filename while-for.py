#name = ['Val', 'Maria', 'Tamires']
#for a in name:
#	print(a)
#----------------------------------
#lista_de_n = range(100, 110, 2)
#for a in lista_de_n:
#	print(a)
#(De 100 a 110 de 2 em 2)
#__________________________________
#----------------------------------
#word = 'Be cool'
#for a in word:  
#	print(a)
#(mostra word em coluna)
#----------------------------------

#i = 1
#while i < 10 :
#	print('Ainda nao >', i)
#	i = i + 1
#----------------------------------

#list_names = ['Ana', 'Laura', 'Bia']
#for x in range(len(list_names)):
#	print(list_names[x])

#----------------------------------

#number_list = range(100, 115)

#number_list1 = range(100, 115)
#b = range(100, 115)

#nome = ['Maria', 'Laura', 'Bia']

#nome.glen(nome)

#print(nome)
from time import sleep

num1 = int(input('Number1: ')) 
num2 = int(input('Number2: '))

op = 0

while op < 6:
	print('''[ 1 ] Somar
[ 2 ] Subtrair
[ 3 ] Dividir
[ 4 ] Multiplicar
[ 5 ] Clear
[ 6 ] EXIT''')
	
	op = int(input('\n>>>Set Option<<<: '))
	if op == 1:
		print()
		print(num1, '+', num2, '=', num1 + num2)
		print()
		sleep(2)
	elif op == 2:
		result = num1 - num2
		print()
		print('{} - {} = {}'.format(num1, num2, result))
		print()
	elif op == 3:
		print(num1 / num2)
	elif op == 4:
		print(num1 * num2)
	elif op == 5:
		print('Set new Numberes:')
		num1 = int(input('Number1: '))
		num2 = int(input('Number2: '))
	elif op == 6:
		print('*' * 40)
		print('{:^40}'.format('FINISHING...'))
		sleep(4)
		print()
	else:
		print('{:-^40}'.format('Invalid Option'))
	print('{:*^40}'.format('*'))
	print('{:*^40}'.format('*'))
	