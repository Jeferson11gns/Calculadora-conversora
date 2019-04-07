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
	result_hex = 0
	cont = 1
	while (hexa >= 16):
		resto_hex = hexa % 16
		hexa = hexa // 16
		result_hex = result_hex * 10 + resto_hex
		cont = cont * 10
		if(hexa < 16):
			result_hex = result_hex + cont * hexa
		
	
	print(result_hex)
	
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
