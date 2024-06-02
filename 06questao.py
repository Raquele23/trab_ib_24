6questao
cidadão = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 16 and idade <18:
	print("Você já pode emitir seu título!")
elif idade >= 18:
	print("Você já deveria ter tirado seu título!")
else:
	print("Você ainda não pode emitir seu título!")
