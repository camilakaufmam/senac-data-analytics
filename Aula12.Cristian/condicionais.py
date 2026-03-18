#Condição para algo: IF

#Digite uma nota (Se nota for maior que 7, o aluno foi aprovado!)
# (Se a nota for menor que 7 e maior ou igual a 5, o aluno esta de recuperação)
# (Se a nota for menor que 5, o aluno esta reprovado)

#EXERCICIO 1:
# nota = float(input("Qual é a sua nota: "))

# if nota >= 7:
#     print("Aprovado!!")
# elif nota >=5: 
#     print("Recuperação!")
# else:
#     print("Reprovado!!")
   
#EXERCICIO 2:
#Crie um algoritmo para saber se um usuário é maior ou menor de idade;

idade = int(input("Qual sua idade? "))

if idade >= 18:
    print("Você é maior de idade")
else: print("Você é menor de idade")