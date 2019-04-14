#cabeçalho
def titulo(msg):
	print("-"*30)
	print("   ", msg)
	print("-"*30)
	

#converter em binario	
def binario(numero):
	result = []
	a = 0
	
	if(numero == 0):
		result.append(numero)
	else:
		while(numero > 0 ):
			if(numero < 2):
				a = numero
				result.append(a)
				numero = numero // 2
			else:
				resto = numero % 2
				numero = numero // 2
				a = resto
				result.append(a)
	
	inverso_result = result[::-1]
	for i in inverso_result:
		print(i, end ="")
	
	print(end="\n")
				

#converter octal
def octal(octa):
	result_octal = []

	if(octa < 8):
		result_octal.append(octa)

	while(octa >= 8):	
		resto_octa = octa % 8
		octa = octa // 8
		result_octal.append(resto_octa) 
		
		if(octa < 8):
			result_octal.append(octa)
		
	
	result_invertido = result_octal[::-1]
	for i in result_invertido:		
		print(i, end="")
	
	print(end="\n")


#analise da letra
def condicaoLetra(letra):
	result_hex = []
	
	if(letra == 10):
		b = "A"
		result_hex.append(b)
	elif(letra == 11):
		b = "B"
		result_hex.append(b)
	elif(letra == 12):
		b = "C"
		result_hex.append(b)
	elif(letra == 13):
		b = "D"
		result_hex.append(b)
	elif(letra == 14):
		b = "E"
		result_hex.append(b)
	elif(letra == 15):
		b = "F"
		result_hex.append(b)
	else:
		result_hex.append(letra)
	
	for y in result_hex:
		return y


#converter hexadecimal
def hexadecimal(hexa):
	respostaCerta = []

	if(hexa < 16 and hexa > 9):
		respostaCerta.append(condicaoLetra(hexa))
	elif(hexa <= 9):
		respostaCerta.append(hexa) 			
	elif(hexa >= 16):
		while (hexa >= 16):
			resto_hex = hexa % 16
			b = resto_hex
			hexa = hexa // 16

			respostaCerta.append(condicaoLetra(b))
		
			if(hexa < 16):
				b = hexa
				respostaCerta.append(condicaoLetra(b))

	inverso_resposta = respostaCerta[::-1] #pega a lista de tras para frente
	print("")
	for y in inverso_resposta:#pecorre a lista
		print(y, end = "")
	
	print("\n")


#de outras bases para decimal
def decimal(numParaSerConvertido, base):
	listaInt1 = []
	listaParaTratarAsLetras = []
	
	if(base == 16):
		for j in numParaSerConvertido:
			if( j == "A" or j == "a" ):
				conversao = 10
				listaParaTratarAsLetras.append(conversao)
			elif(j == "B" or j == "b"):
				conversao = 11
				listaParaTratarAsLetras.append(conversao)
			elif(j == "C" or j == "c"):
				conversao = 12
				listaParaTratarAsLetras.append(conversao)
			elif(j == "D" or j == "d"):
				conversao = 13
				listaParaTratarAsLetras.append(conversao)
			elif(j == "E" or j == "e"):
				conversao = 14
				listaParaTratarAsLetras.append(conversao)
			elif(j == "F" or j == "f"):
				conversao = 15
				listaParaTratarAsLetras.append(conversao)
			else:
				listaParaTratarAsLetras.append(j)
	else:
		for j in numParaSerConvertido:
			listaParaTratarAsLetras.append(j)
	

	for i in listaParaTratarAsLetras:
		listaInt1.append(int(i))

	listaInvertida = listaInt1[::-1]
	
	a=[]
	b= []
	cont = 0
	for j in range(len(listaInt1)):
		a.append(base**j)
		cont = cont + 1
		
	for k in listaInvertida:
		b.append(k)

	soma = 0
	while( cont != 0):
		soma = soma + a[cont-1]*b[cont-1]
		cont = cont - 1
	
	print(soma, end="\n")


#soma de binario
def somaBin(num1, num2):
	listaInt1 = []
	listaInt2 = []
	
	for i in num1:
		listaInt1.append(int(i))

	for j in num2:
		listaInt2.append(int(j)) 

	
	
	#print(soma)
	print(listaInt1)
	print(listaInt2)


#programa principal
titulo("Menu Inicial")

print("1 - Converter\n2 - Soma de binario")
menu = int(input("Escolha a opção: "))
print("\n")

#if para entrar no menu inicial
if(menu == 1): 
	titulo("menu do converter")
	
	print(" 1- Decimal para binario\n",
	"2- Decimal para octal\n",
	"3- Decimal para hexadecimal\n",
	"4- Binario para decimal\n",
	"5- Octal para decimal\n",
	"6- Hexadecimal para decimal")
	converter = int(input(" Escolha a opção: "))
		
	if(converter == 1):
		binario(int(input(" Digite o numero em decimal: ")))
	elif(converter == 2):
		octal(int(input(" Digite o numero em decimal: ")))
	elif(converter == 3):
		hexadecimal(int(input(" Digite o numero em decimal: ")))
	elif(converter == 4):
		decimal(str(input(" Digite o numero em binario: ")), 2)
	elif(converter == 5):
		decimal(str(input(" Digite o numero em octal: ")), 8)
	elif(converter == 6):
		decimal(str(input(" Digite o numero em Hexadecimal: ")), 16)
		
else:
	titulo("menu do soma binaria")
	somaBin(str(input("digite o primeiro ")), str(input("digite o segundo ")) )
