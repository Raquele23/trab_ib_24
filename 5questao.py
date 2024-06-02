5questao -teste-
hora = int(input("Diga um número entre 0 e 23: "))
if hora >= 5 and hora < 12:
	print("Está de manhã")
elif hora >= 12 and hora <= 17:
	print("Já está de tarde")	
else:
	print("Está de noite")
