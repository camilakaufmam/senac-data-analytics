# Titulo
## Subtitulo
#### ate quamtos tu quiser

```python
# trecho de codigo dentro das crases
```

## Booleanos sao frequentemente resultado de comparacoes
```python
idade = 20
nota = 7.5

print(f"idade > 18: {idade > 18}")
print(f"idade == 20: {idade == 20}")
print(f"nota >= 7: {nota >= 7}")
print(f"nota < 5: {nota < 5}")
```

## Uso do len
```python
# String vazia
#len quer dizer quantos caracteres tem na celula
texto_vazio = ","
print(f"String vazia: '{texto_vazio}'")
print(f"Tamanho: {len(texto_vazio)} caracteres")
```

## Tranformando Tipos
```python
inteiro = 10
float1 = 15.69998
print(f"Tranfornando inteiro em float: {float(inteiro)}") # 10.0
print(f"Tranfornando inteiro em boolean: {bool(inteiro)}") # true pq é diferente de zero
print(f"Tranfornando inteiro em texto: {str(inteiro)}") # "10" 
print(f"Tranfornando float em inteiro:{int(float1)}") # 15
```
## Operadores de Atribuicao Composta
```python
x = 10
x += 5 #quer dizer x = x + 5
x -= 5 #quer dizer x = x - 5
x *= 5 #quer dizer x = x * 5
x /= 5 #quer dizer x = x / 5
x //= 5 #quer dizer x = x / 5 POREM, sempre com número inteiro
x **= 5 #quer dizer x = x elevado a 5ª potencia
x %= 5 #quer dizer Resto da divisao (modulo)
# COM STRING:
texto = "Ola"
texto += " Mundo"     # Concatenacao, fica: "Ola Mundo"
linha = "-"
linha *= 20           # Repeticao, fica 20 vezes -----
```
# LISTA
```python
#Lista sem com COLCHETES []
#Lembrando que a lista começa com zero. Se quero trazer o primeiro valor, tenho que indicar 0
frutas = ["maça", "banana", "uva", "pera", "abacaxi"]
print(f"Primeira fruta: {frutas[0]}") #traz o primeiro valor
print(f"Segunda fruta: {frutas[1]}") #traz o segundo valor
print(f"Ultima fruta:{frutas[-1]}") #traz o ultimo valor
print(f"Penultima fruta:{frutas[-2]}") #traz o penultimo valor
frutas[0] = "morango" #Sobreescrevendo o primeiro item da lista
frutas.append("mamao") #Vai acrescentar mamao na ultima posicao da lista
frutas.remove("uva") #Vai remover a uva da lista
```
# TUPLA
```python
# Tuplas - semelhantes a listas, mas NAO podem ser alteradas
#A difença para lista é que se usa parenteses e é imutavel. Ex.:
fruta = ("maça","mamao", "limao")
```
# DICIONARIO
```python
#