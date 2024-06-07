np = int(input("Escolha um número de 0 a 10: "))
nb = int(input("Escolha um número de 0 a 10: "))
print(".               "); print(".               ")
print("BOLETIM ESCOLAR")
aluno = input("Digite o nome e sobrenome do aluno: ")
disciplina = input("Digite o nome da disciplina: ")
print("                ")
media = (np + nb)/2
if media >= 6:
  print(f"{aluno} está APROVADO na disciplina de {disciplina}!")
else:
  print(f"{aluno} está REPROVADO na disciplina de {disciplina}!")