# Trabalhando com Listas em Python 📝 🐍
## Criando listas
Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto. 
Podemos criar listas utilizando o construtor **list**, a função range ou colocando 
valores separados por vírgula dentro de colchetes. Listas são objetos mutáveis, 
portanto podemos alterar seus valores após criação.

**exe:**

 `frutas = ["laranja", "maca", "uva"]`
 
 `frutas = []`
 
 `letras = list("python")`
 
 `numeros = list(range(10))`
 
 `carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]` 

#### Acesso direto
A lista é uma sequência, portanto podemos acessar seus dados utilizando índices. 
Contamos o índice de determinada sequência a partir do zero.

**exe:**

`frutas = ["maçã", "laranja", "uva", "pera"]`

`frutas[0]  # maçã`

`frutas[2]  # uva`

#### Índices negativos
Sequências suportam indexação negativa. A contagem começa em -1.

**exe:**

`frutas = ["maçã", "laranja", "uva", "pera"]`

`frutas[-1]  # pera`

`frutas[-3]  # laranja`

#### Listas aninhadas
Listas por serem objetos podem armazenar todos os tipos de objetos do Python, portanto 
podemos ter listas que armazenam outras listas. Com isso podemos criar estruturas 
bidimensionais (tabelas), e acessar iformando os indíces de linha e coluna.

**exe:**

`matriz = [`

`[1, "a", 2],`

`["b", 3, 4],`

`[6, 5, "c"]`

`]`

`matriz[0]  # [1, "a", 2]`

`matriz[0][0]  # 1`

`matriz[0][-1]  # 2`

`matriz[-1][-1]  # "c"`

#### Fatiamento
Além de acessar elementos diretamente, podemos extrair um conjutno de valores de uma 
sequência. Para isso basta passar o índice inicial e/ou final para acessar o conjunto. 
Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

**exe:**

`lista = ["p", "y", "t", "h", "o", "n"]`

`lista[2:]  # ["t", "h", "o", "n"]`

`lista[:2]  # ["p", "y"]`

`lista[1:3]  # ["y", "t"]`

`lista[0:3:2]  # ["p", "t"]`

`lista[::]  # ["p", "y", "t", "h", "o", "n"]`

`lista[::-1]  # ["n", "o", "h", "t", "y", "p"]`

#### Iterar listas
A forma mais comum pata percorrer os dados de um lista é utilizando o comando **for**

**exe:**

`carros = ["gol", "celta", "palio"]`

 `for carro in carros:`
 
      `print(carro)`

#### Função enumerate
Às vezes é necessário saber qual é o índice do objeto dentro do laço **for**. Por 
isso podemos usar a função **enumerate**.

**exe:**

`carros = ["gol", "celta", "palio"]`

`for indice, carro in enumerate(carros):`

    `print(f"{indice}: {carro}")`

#### Compreensão de listas
A compreensão de lista oferece uma sintaxe mais curta quando você deseja: criar 
uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova
lista aplicando alguma modificação nos elementos de uma lista existente.

**exe:**

**Filtro versão 1**

`numeros = [1, 30, 21, 2, 9, 65, 34]`

`pares = []`

`for numero in numeros:`

    `if numero % 2 == 0:`

        `pares.append(numero)`
        
**Filtro boas práticas**

`numeros = [1, 30, 21, 2, 9, 65, 34]`

`pares = [numero for numero in numeros if numero % 2 == 0]`

**Modificando valores da versao 1**

`numeros = [1, 30, 21, 2, 9, 65, 34]`

`quadrado = []`

`for numero in numeros:`

`quadrado.append(numero ** 2)`

**Modificando valores da versao boas praticas**

`numeros = [1, 30, 21, 2, 9, 65, 34]`

`quadrado = [numero ** 2 for numero in numeros]`

### Métodos da classe list

**[].append**

O método append é utilizado para adicionar um novo objeto a uma lista existente

**exe:**

`lista = []`

`lista.append(1)`

`lista.append("Python")`

`lista.append([40, 30, 20])`

`print(lista)  # [1, "Python", [40, 30, 20]]`

**[].clear**

O método clear é utilizado para apagar todos os objetos contidos em uma lista

**exe:**

`lista = [1, "Python", [40, 30, 20]]`

`print(lista)  # [1, "Python", [40, 30, 20]]`

`lista.clear()`

`print(lista)  # []`

**[].copy**

O método copy é utilizado para retornar uma lista idêntica a lista original, podendo assim fazer alterações na lista copiada mantendo a original.

**exe:**

`lista = [1, "Python", [40, 30, 20]]`

`l2 = lista.copy()`

`print(lista)  # [1, "Python", [40, 30, 20]]`

`print(id(l2), id(lista)) # 139903141989440, 139903141929704`

`l2[0] = 2`

`print (l2) # [2, "Python", [40, 30, 20]]`

`print (lista) # [1, "Python", [40, 30, 20]]`

**[].count**

O método count é utilizado para saber quantas vezes um determinado objeto aparece na lista

**exe:**

`cores = ["vermelho", "azul", "verde", "azul"]`

`cores.count("vermelho")  # 1`

`cores.count("azul")  # 2`

`cores.count("verde")  # 1`

**[].extend**

O método extend é utlizado para adicionar vários objetos ao mesmo tempo em uma lista existente porém ele não exclui valores duplicados.

**exe:**

`linguagens = ["python", "js", "c"]`

`print(linguagens)  # ["python", "js", "c"]`

`linguagens.extend(["java", "csharp"])`

`print(linguagens)  # ["python", "js", "c", "java", "csharp"]`

**[].index**

O método index é utilizado para se ter conhecimento em que posição os objetos se encontram ( ele retorna somente a primeira ocorrência de um objeto).

**exe:**

`linguagens = ["python", "js", "c", "java", "csharp"]`

`linguagens.index("java")  # 3`

`linguagens.index("python")  # 0`

**[].pop**

O método pop é utilizado para retirar o último elemento da lista, porém pode se passar o indice de qual objeto se quer remover.

**exe:**

linguagens = ["python", "js", "c", "java", "csharp"]

`linguagens.pop()  # csharp`

`linguagens.pop()  # java`

`linguagens.pop()  # c`

`linguagens.pop(0)  # python`

**[].remove**

O método remove é utilizado para remover um objeto de uma lista, nesse caso diferente do pop se utiliza o próprio objeto.

**exe:**

`linguagens = ["python", "js", "c", "java", "csharp"]`

`linguagens.remove("c")`

`print(linguagens)  # ["python", "js", "java", "csharp"]`

**[].reverse**

O método reverse é utilizado para fazer com que uma lista fique ao contrário

**exe:**

`linguagens = ["python", "js", "c", "java", "csharp"]`

`linguagens.reverse()`

`print(linguagens)  # ["csharp", "java", "c", "js", "python"]`

**[].sort**

O método sort é utilizado para ordenar uma lista

**exe:**

`linguagens = ["python", "js", "c", "java", "csharp"]`

`linguagens.sort()  # ["c", "csharp", "java", "js", "python"]`

`linguagens = ["python", "js", "c", "java", "csharp"]`

Utilizando o argumento **reverse=True** ele ordena com o espelhamento

`linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]` 

`linguagens = ["python", "js", "c", "java", "csharp"]`

Utilizando a função anomina com o argumento x **(key=lambda x:len(x))** ele ordena a lista de acordo com o tamanho de cada objeto.

`linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]`

`linguagens = ["python", "js", "c", "java", "csharp"]`

Utilizando a combinação de **(key=lambda x:len(x)) com o reverse=True** ele ordena a lista de acordo com o tamanho de cada objeto espelhada.

`linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]`

**[].len**

O método len é utilizado para saber a quantidade de objetos contidos em uma lista

**exe:**

`linguagens = ["python", "js", "c", "java", "csharp"]`

`len(linguagens)  # 5`

**sorted**

O sorted é uma função que serve para ordenar iteraveis. (é basicamente a mesmo que o [].sort porém aqui ele se apresenta como uma função)

**exe:**

`linguagens = ["python", "js", "c", "java", "csharp"]`

`sorted(linguagens, key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]`

`sorted(linguagens, key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]`

## Conhecendo Tuplas em Python
### Criando Tuplas
Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto lsitas são mutáveis. podemos criar tuplas através da classe **tuple**, ou colocando valores separados por vírgulas de parenteses.

**exe:**

`frutas = ("laranja", "pera", "uva",)`

`letras = tuple("python")`

`numeros = tuple([1, 2, 3, 4])`

`pais = ("Brasil",)`

#### Acesso direto
A tupla é uma sequência, portanto podemos acessar seus dados utilizando índices. Contamos o índice de determinada sequência a partir do zero.

**exe:**

`frutas = ["maçã", "laranja", "uva", "pera"]`

`frutas[0]  # maçã`

`frutas[2]  # uva`

#### Indíces negativos

Sequências suportam indexação negativa. A contagem começa em -1.

**exe:**

`frutas = ["maçã", "laranja", "uva", "pera"]`

`frutas[-1]  # pera`

`frutas[-3]  # laranja`

#### Tuplas aninhadas
Tuplas podem armazenar todos os tipos de objetos em Python, portanto podemos ter tuplas que armazenam outras tuplas. Com isso podemos criar estruturas bidimensionais (tabelas), e acessar informando os índices de linha e coluna.

**exe:**

`matriz = [`

`[1, "a", 2],`

`["b", 3, 4],`

`[6, 5, "c"]`

`]`

`matriz[0]  # [1, "a", 2]`

`matriz[0][0]  # 1`

`matriz[0][-1]  # 2`

`matriz[-1][-1]  # "c"`
#### Fatiamento
Além de acessar elementos diretamente, podemos extrair um conjunto de valores de uma sequência. Para isso basta passar o índice inicial e/ou final para acesssar o conjunto. Podemos ainda informar quantas posições o cursor deve "pular" no acesso.

**exe:**

`lista = ["p", "y", "t", "h", "o", "n"]`

`lista[2:]  # ["t", "h", "o", "n"]`

`lista[:2]  # ["p", "y"]`

`lista[1:3]  # ["y", "t"]`

`lista[0:3:2]  # ["p", "t"]`

`lista[::]  # ["p", "y", "t", "h", "o", "n"]`

`lista[::-1]  # ["n", "o", "h", "t", "y", "p"]`

### Métodos da classe tupla

**[].count**

O método count é utilizado para saber quantas vezes um determinado objeto aparece na lista

**exe:**

`cores = ["vermelho", "azul", "verde", "azul"]`

`cores.count("vermelho")  # 1`

`cores.count("azul")  # 2`

`cores.count("verde")  # 1`

**[].index**

O método index é utilizado para se ter conhecimento em que posição os objetos se encontram ( ele retorna somente a primeira ocorrência de um objeto).

**exe:**

`linguagens = ["python", "js", "c", "java", "csharp"]`

`linguagens.index("java")  # 3`

`linguagens.index("python")  # 0`

**[].len**

**exe:**

O método len é utilizado para saber a quantidade de objetos contidos em uma lista

`linguagens = ["python", "js", "c", "java", "csharp"]`

`len(linguagens)  # 5`
