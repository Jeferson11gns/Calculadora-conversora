#cabeçalho
def titulo(msg):
	print("-"*30)
	print("   ", msg  )
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
	
	inverso = result[::-1]
	for x in inverso:
		print(x, end ="")
					
#converter octal
def octal(octa):
	result_octal = 0
	cont = 1
	if(octa < 8):
		result_octal = octa
	while(octa >= 8):	
		resto_octa = octa % 8
		octa = octa // 8
		result_octal = result_octal * 10 + resto_octa
		cont = cont * 10
		if(octa < 8):
			result_octal = result_octal + cont * octa
			
	print(result_octal)
	
#converter hexadecimal
def hexadecimal(hexa):
	result_hex = []
	if(hexa < 16):
		if(hexa == 10):
			b = "A"
			result_hex.append(b)
		elif(hexa == 11):
			b = "B"
			result_hex.append(b)
		elif(hexa == 12):
			b = "C"
			result_hex.append(b)
		elif(hexa == 13):
			b = "D"
			result_hex.append(b)
		elif(hexa == 14):
			b = "E"
			result_hex.append(b)
		elif(hexa == 15):
			b = "F"
			result_hex.append(b)
	else:
		while (hexa >= 16):
			resto_hex = hexa % 16
			b = resto_hex
			hexa = hexa // 16
			
		
			if(resto_hex == 10):
				b = "A"
				result_hex.append(b)
			elif(resto_hex == 11):
				b = "B"
				result_hex.append(b)
			elif(resto_hex == 12):
				b = "C"
				result_hex.append(b)
			elif(resto_hex == 13):
				b = "D"
				result_hex.append(b)
			elif(resto_hex == 14):
				b = "E"
				result_hex.append(b)
			elif(resto_hex == 15):
				b = "F"
				result_hex.append(b)
			else:
				result_hex.append(b) #pega o resto e adiciona a lista			

			if(hexa < 16):
				b = hexa
				result_hex.append(b)

	inverso_hex = result_hex[::-1] #pega a lista de tras para frente
	for y in inverso_hex:#pecorre a lista
		print(y, end = "")
	



#soma de binario
def somaBin(num1, num2):
	listaInt1 = []
	listaInt2 = []
	listaInt1.append(num1) 
	listaInt2.append(num2)

	for i in listaInt1:
		print(i)
	for j in listaInt2:
		print(j)
	
	soma = i + j
	
	print(soma)
	print(listaInt1)
	print(listaInt2)
	
#programa principal
titulo("Menu Inicial")

print("\n1 - Converter\n2 - Soma de binario")
menu = int(input(""))
print("\n")

#if para entrar no menu inicial
if(menu == 1): 
	titulo("menu do converter")
	print(" 1- decimal para binario\n",
	"2- decimal para octal\n",
	"3- decimal para hexadecimal\n",
	"4- binario para decimal\n",
	"5- octal para decimal\n",
	"6- hexadecimal para decimal")
	converter = int(input())
	
	if(converter == 1):
		binario(int(input("Digite o numero: ")))
	elif(converter == 2):
		octal(int(input("Digite o numero: ")))
	elif(converter == 3):
		hexadecimal(int(input("Digite o numero: ")))	
else:
	titulo("menu do soma binaria")
	somaBin(str(input("digite o primeiro ")), str(input("digite o segundo ")) )
