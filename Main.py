from SomaDeBinario import *
from Convercoes import *


def titulo(msg):
	print("-"*30)
	print("   ", msg)
	print("-"*30)
	


titulo("Menu Inicial")

print("1 - Converter\n2 - Soma de binario")
menu = int(input("Escolha a opção: "))
print("\n")


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
