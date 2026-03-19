#Ler dois números e calcular a SOMA, SUBTRAÇÃO, DIVISÃO E MULTIPLICAÇÃO

#1º - Entrada de Dados:
    #coloquei FLOAT pois o resultado de uma divisão pode não ser número inteiro
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#2º Processamento:
soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

#3º Saida de Dados (Exibição)
    #Fiz de duas formas para trazer as variáveis(com "chaves" e "vírgula")
print(f"A soma é:  {soma :.1f}" )
print(f"A subtração é: ", subtracao)
print(f"A divisão é: {divisao :.2f}")
print(f"A multiplicação é:" , multiplicacao )

#Limpar o terminal: digita "cls" e enter

#SEGUNDO EXERCÍCIO:

#print (f"multiplicacao: {multiplicação}")

#Quantos anos eu terei daqui a 10 anos?

idade = int(input("Quantos anos você tem? "))
num = 10
multiplicacao = idade + num

print(f"Sua idade daqui a 10 anos será: {multiplicacao} anos")