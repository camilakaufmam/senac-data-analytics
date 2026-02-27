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
```

# AULA 6
```python
# SEMPRE IRÁ USAR O "encoding='utf-8"
with open('turma.json', 'r', encoding='utf-8') as f:

```


# AULA 7
```python
#                       NUMPY (biblioteca focada em dados matematicos rapidos e manipulação de Arrays (vetores e matrizes)):
# 
#Fatiamento [inicio:fim:passo] =    Slicing 
print('Primeiras 3:      ', notas[:3])           # indices 0,1,2
print('Ultimas 3:        ', notas[-3:])          # ultimos 3
print('Indices 2 a 5:    ', notas[2:5])          # 2,3,4
print('Passo de 2:       ', notas[::2])          # 0,2,4,6
print('Invertido:        ', notas[::-1])"


# EX.: print('Prova 1 de todos:  ', turma[:, 0])     # coluna 0   USAR ":," PARA SE REFERIR A COLUNA

#Funcoes de Agregacao:
notas = np.array([7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 5.5, 9.5])

print('Notas:', notas)
print()
print(f'Soma:          {np.sum(notas)}')
print(f'Media:         {np.mean(notas):.2f}')   #MEDIA
print(f'Mediana:       {np.median(notas):.2f}')
print(f'Desvio padrao: {np.std(notas):.2f}')
print(f'Variancia:     {np.var(notas):.2f}')
print(f'Minimo:        {np.min(notas)}')        #POSIÇÃO DO MENOR VALOR
print(f'Maximo:        {np.max(notas)}')        #POSIÇÃO DO MAIOR VALOR
print(f'Indice do min: {np.argmin(notas)}')   #
print(f'Indice do max: {np.argmax(notas)}')   #

# Reshape — muda o formato sem alterar os dados
a = np.arange(1, 13)      # [1, 2, 3, ..., 12]
print('Original (1D):', a)

# Transpose — inverte linhas e colunas
m = np.array([[1, 2, 3],
              [4, 5, 6]])

print('Original (2x3):')

#CONCATENAÇÃO:
# Concatenar arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Horizontalmente (1D)
h = np.concatenate([a, b])
print('Concatenado:', h)

# Forca um tipo especifico
a_float32 = np.array([1, 2, 3], dtype=np.float32)

print(f'Inteiro:   {a_int.dtype}')

# np.diff  calcula diferenca entre dias consecutivos
#EX.:
diferenca_temperaturas = np.diff(temperaturas)
print(f"A diferença de temperatura é: {np.around(diferenca_temperaturas, 1)}")
#EXPLICAÇÃO: 
# np.diff(temperaturas) → calcula a diferença entre valores consecutivos do array.
#np.around(..., 1) → arredonda para 1 casa decimal.
#f"" → permite inserir a variável diretamente no texto.



#               PANDAS (funciona em cima do Numpay, Organiza dados em formato de tabela, como no Excel):


#               O **groupby** divide o DataFrame em grupos, aplica uma funcao e combina os resultados.

# Multiplas funcoes de agregacao com .agg()
resumo = vendas.groupby('vendedor').agg(
    total_vendas  = ('valor', 'sum'),
    media_venda   = ('valor', 'mean'),
    qtd_transacoes= ('valor', 'count'),
    max_venda     = ('valor', 'max')
).round(2)

print('Resumo por vendedor:')

## Resumo — Principais Funcoes

### NumPy

| Funcao | Descricao |
|--------|-----------|
| `np.array()` | Cria um array |
| `np.zeros()`, `np.ones()`, `np.full()` | Arrays com valores fixos |
| `np.arange()`, `np.linspace()` | Sequencias |
| `np.random.rand()`, `np.random.randn()`, `np.random.randint()` | Numeros aleatorios |
| `arr.shape`, `arr.ndim`, `arr.dtype` | Atributos do array |
| `arr.reshape()`, `arr.T` | Reformatar e transpor |
| `np.sum()`, `np.mean()`, `np.std()`, `np.min()`, `np.max()` | Agregacoes |
| `np.sqrt()`, `np.abs()`, `np.exp()`, `np.log()` | Matematica |
| `np.concatenate()`, `np.vstack()`, `np.hstack()` | Combinar arrays |

### Pandas

| Funcao / Metodo | Descricao |
|----------------|-----------|
| `pd.Series()`, `pd.DataFrame()` | Criar estruturas |
| `pd.read_csv()`, `df.to_csv()` | I/O de arquivos |
| `df.head()`, `df.tail()`, `df.info()`, `df.describe()` | Inspecionar |
| `df['col']`, `df[['c1','c2']]` | Selecionar colunas |
| `df.loc[]`, `df.iloc[]` | Selecionar por rotulo/posicao |
| `df[condicao]` | Filtrar linhas |
| `df.sort_values()` | Ordenar |
| `df.groupby().agg()` | Agrupar e agregar |
| `pd.merge()`, `pd.concat()` | Combinar DataFrames |
| `df.isnull()`, `df.fillna()`, `df.dropna()` | Tratar nulos |
| `df['col'].str.xxx` | Operacoes com strings |
| `df['col'].dt.xxx` | Operacoes com datas |
| `pd.pivot_table()`, `pd.crosstab()` | Tabelas cruzadas |




```