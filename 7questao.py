7questao
np = int(input("Escolha um número de 0 a 10: "))
nb = int(input("Escolha um número de 0 a 10: "))
print("BOLETIM ESCOLAR")
aluno = input("Digite o nome do aluno: ")
disciplina  = input("Digite o nome da disciplina: ")
print(f"A nota parcial do aluno foi {np + .0} e a nota bimestral {nb + .0}")
media = (np + nb)/2
if media >= 6:
  print(f"{aluno} ficou com a média de {media}, portanto está APROVADO na disciplina de {disciplina}!")
else:
  print(f"{aluno} ficou com a média de {media}, portanto está REPROVADO na disciplina de {disciplina}!")
