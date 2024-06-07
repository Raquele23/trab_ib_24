hora = int(input("Diga um número entre 0 e 23: "))
if hora < 12:
	print("Está de manhã!")
elif hora >= 12 and hora <= 17:
	print("Está de tarde!")	
else:
	print("Está de noite!")