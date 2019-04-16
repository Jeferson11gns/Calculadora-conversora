
#soma de binario
def somaBin(num1, num2):
	listaInt1 = []
	listaInt2 = []
	inverso = []
	inverso2 = []

	for i in num1:
		listaInt1.append(int(i))
	for j in num2:
		listaInt2.append(int(j))

	inverso = listaInt1[::-1]
	inverso2 = listaInt2[::-1]

	vai = 0
	soma = 0
	somaFinal = []
	
	for k in range(len(inverso)):
		soma = inverso[k] + inverso2[k]
		
		if((soma + vai) == 3 or (soma + vai == 1)):
			somaFinal.append(1)
		elif(soma + vai == 2 or soma + vai == 0):
			somaFinal.append(0)
		
		if(soma + vai == 3 or soma + vai == 2):
			vai = 1
		elif(soma + vai == 1 or soma + vai == 0):
			vai = 0
		
	if(soma + vai >= 2):
		somaFinal.append(1)
		
	for i in somaFinal[::-1]:
	    print(i, end="")
	
	print("\n")