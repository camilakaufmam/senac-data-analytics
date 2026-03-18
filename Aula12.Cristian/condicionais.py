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

# idade = int(input("Qual sua idade? "))

# if idade >= 18:
#     print("Você é maior de idade")
# else: 
#     print("Você é menor de idade")

#EXERCICIO 3:
#Crie um algoritmo que pergunte a idade;
#se a idade for menor que 12, então ecreva "Você é um criança";
#se a idade for menor que 18, então ecreva "Você é um adolescente";
#se a idade for menor que 70, então ecreva "Você é um adulto";
#senão, escreva "Você é um idoso";


idade = int(input("Qual sua idade? "))

if idade <= 12:
    print("Você é um criança")
elif idade <= 18:
    print("Você é um adolescente")
elif idade <=70:
    print("Você é um adulto")
else:
    print("Você é um idoso")