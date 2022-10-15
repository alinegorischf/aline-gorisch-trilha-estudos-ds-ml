# Anotações cursos Python Intermediário

Cursos da trilha de cientista de dados

Nível: Intermediário

Carga horária: 8h

Skills: Python, Data

# Curso 6: Trabalhando com Listas em Python 📝 🐍
## Listas: Criação e acessos aos dados
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

## Métodos da classe list

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

# Curso 7: Conhecendo Tuplas em Python 🐍 📝
## Criando Tuplas
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

## Métodos da classe tupla

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

##  Curso 8: Explorando conjuntos em Python 🐍 📝
## Como crair conjuntos
Um **set** é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.

**exe:**

`set([1, 2, 3, 1, 3, 4])  # {1, 2, 3, 4}`

`set("abacaxi")  # {"b", "a", "c", "x", "i"}`

`set(("palio", "gol", "celta", "palio"))  # {"gol", "celta", "palio"}`

#### Acessando os dados

Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os seus valores é necessário **converter** o conjunto para lista.

**exe:**

`numeros = {1, 2, 3, 2}`

`numeros = list(numeros)`

`numeros[0]`

#### Iterar conjuntos

A forma mais comum para percorrer os dados de um conjunto é utilizando o comando **for**

**exe:** 

`carros = {"gol", "celta", "palio"}`

`for carro in carros:`

`print(carro)`

#### Função enumerate

Às vezes é necessário saber qual índice do objeto dentro do laço **for**. Para isso podemos usar a função **enumerate.**

*exe:**

`carros = {"gol", "celta", "palio"}`

`for indice, carro in enumerate(carros):``

`print(f"{indice}: {carro}")`


## Métodos da classe set

**{}.union**

O método **union** é utlizado para fazer a junção de dois conjuntos

**exe:**

`conjunto_a = {1, 2}`

`conjunto_b = {3, 4}`

`conjunto_a.union(conjunto_b)  # {1, 2, 3, 4}`

![image](https://user-images.githubusercontent.com/112986146/195988713-c23569bf-3f35-4eff-86c9-6ec54536d68f.png)

**{}.intersection**

O método **intersection** é utlizado para ver a intersecção de dois conjuntos

**exe:**

`conjunto_a = {1, 2, 3}`

`conjunto_b = {2, 3, 4}`

`conjunto_a.intersection(conjunto_b)  # {2, 3}`

![image](https://user-images.githubusercontent.com/112986146/195988851-e2822129-6f20-49a4-8762-9c1b4a655e27.png)

**{}.difference**

O método **difference** é utlizado para ver tudo o que está em um conjunto mas que não aparece no outro conjunto

**exe:**

`conjunto_a = {1, 2, 3}`

`conjunto_b = {2, 3, 4}`

`conjunto_a.difference(conjunto_b)  # {1}`

`conjunto_b.difference(conjunto_a)  # {4}`

![image](https://user-images.githubusercontent.com/112986146/195988971-df0b58f0-83dc-4a79-a63b-0397382250d5.png)

**{}.symmetric_difference**

O método **symmetric_ddifference** é utlizado para ver todos os elementos que não se econtram na intersecção

**exe:**

`conjunto_a = {1, 2, 3}`

`conjunto_b = {2, 3, 4}`

`conjunto_a.symmetric_difference(conjunto_b)  # {1, 4}`

![image](https://user-images.githubusercontent.com/112986146/195989083-76475fee-a89e-4468-8e2e-cf8b398a2813.png)

**{}.issubset**

O método **issubset** é utilizado para verificar pertencimentos de conjuntos e o seu resultado será booleano 

**exe:**

`conjunto_a = {1, 2, 3}`

`conjunto_b = {4, 1, 2, 5, 6, 3}`

`conjunto_a.issubset(conjunto_b)  # True`

`conjunto_b.issubset(conjunto_a)  # False`


![image](https://user-images.githubusercontent.com/112986146/195989307-3104fd3d-8dbb-41de-b727-8d363273ea4f.png)

**{}.isdisjoint**

O método **isdisjoint** é utilizado para verificar conjuntos que são disjuntos, ou seja um conjunto contém elementos de outro conjunto

`conjunto_a = {1, 2, 3, 4, 5}`

`conjunto_b = {6, 7, 8, 9}`

`conjunto_c = {1, 0}`

`conjunto_a.isdisjoint(conjunto_b)  # True`

`conjunto_a.isdisjoint(conjunto_c)  # False`

![image](https://user-images.githubusercontent.com/112986146/195989577-0b564ded-63ca-4933-a0b0-56c58e7fd496.png)

**{}.add**

O método **add** é utilizado para adicionar elementos que não existem em um conjunto

**exe:**

`sorteio = {1, 23}`

`sorteio.add(25)  # {1, 23, 25}`

`sorteio.add(42)  # {1, 23, 25, 42}`

`sorteio.add(25)  # {1, 23, 25, 42}`

**{}.clear**

O método **clear** é utilizado para limpar um conjunto

**exe:**

`sorteio = {1, 23}``

`sorteio  # {1,23}`

`sorteio.clear()`

`sorteio  # {}`

**{}.copy**

O método **copy** é utilizado para gerar um cópia de um conjunto
**exe:**

`sorteio = {1, 23}``

`sorteio  # {1,23}`

`sorteio.copy()`

`sorteio  # {1, 23}`


**{}.discard**

O método **discard** é utilizado para descartar um valor de um conjunto e somente valores existentes serão descartados

**exe:**

`numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}`

`numeros  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}`

`numeros.discard(1)`

`numeros.discard(45)`

`numeros  # {2, 3, 4, 5, 6, 7, 8, 9, 0}`


**{}.pop**

O método **pop** é utilizado para retirar valores, ele começa sempre pelos primeiros valores formando então uma sequência.

**exe:**

`numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}`

`numeros  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`

`numeros.pop()  # 0`

`numeros.pop()  # 1`


`numeros  # {2, 3, 4, 5, 6, 7, 8, 9}`

**{}.remove**

O método **remove** é utilizado para remover valores podendo se utilizar como argumento o valor a ser removido e caso esse valor não exista ele retorna uma mensagem de erro.

**exe:**

`numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}`

`numeros  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`

`numeros.remove(0)  # 0`

`numeros  # {1, 2, 3, 4, 5, 6, 7, 8, 9}`

**{}.len**

O método **len** é utilizado para retornar o tamanho de um conjunto
**exe:**

`numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}`

`len(numeros)  # 10`

**{}.len**

O método **in** é utilizado para verificar se um elemento esta dentro de um conjunto

**exe:**

`numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}`

`1 in numeros  # True`

`10 in numeros  # False`

# Curso 9: Aprendendo a Utilizar dicionários em Python 🐍 📝
## Dicionários: Criação e acesso aos dados
### Criando dicionários
Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas. Não permite chaves repetidas ele sobreescreve os valores.

**exe:**

`pessoa = {"nome": "Guilherme", "idade": 28}`

`pessoa = dict(nome="Guilherme", idade=28)`

`pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}`

### Acesso aos dados
Os dados são acessados e modificados através da chave.

**exe:**

`dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}`

`dados["nome"]  # "Guilherme"`

`dados["idade"]  # 28`

`dados["telefone"]  # "3333-1234"`

`dados["nome"] = "Maria"`

`dados["idade"] = 18`

`dados["telefone"] = "9988-1781"`

vdados  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}`

### Dicionários aninhados
Dicionários aninhados podem armazenar qualque tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável como (strings e números)

contatos = {

   `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},`
   
   `"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},`
   
   `"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},`
   
   `"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},`
`}`

`contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"`

### Iterar dicionários
A forma mais comum para percorrer os dados de um dicionário é utilizando o comando **for**

**exe:**
`for chave in contatos:` #método não recomendado

    `print(chave, contatos[chave])`
    
`for chave, valor in contatos.items():`

    `print(chave, valor)`
    
`guilherme@gmail.com {'nome': 'Guilherme', 'telefone': '3333-2221'}`

`giovanna@gmail.com {'nome': 'Giovanna', 'telefone': '3443-2121'}`

`chappie@gmail.com {'nome': 'Chappie', 'telefone': '3344-9871'}`

`melaine@gmail.com {'nome': 'Melaine', 'telefone': '3333-7766'}`

## Métodos da classe dict

**{}.clear**

O método **clear** apaga todos os valores do dicionário

*exe:**

`contatos = {`

     `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},`
    
     `"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},``
    
    `"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},```
    
    `"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},`
`}`
`contatos.clear()`
`contatos  # {}`

**{}.copy**

O método **copy** ele faz uma cópia do dicionário

**exe:**

`contatos = {`
    
    `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}`
`}`

`copia = contatos.copy()`

`copia["guilherme@gmail.com"] = {"nome": "Gui"}`

`contatos["guilherme@gmail.com"]  # {"nome": "Guilherme", "telefone": "3333-2221"}`

`copia["guilherme@gmail.com"]  # {"nome": "Gui"}`

**{}.fromkeys**

O método **fromkeys** cria chaves vazias ou com um valor padrão de uma vez só

**exe:**

`dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}`

`dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}`

**{}.get**

O método **get** acessa valores do dicionário

**exe:**

`contatos = {`

    `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}`
`}`

`contatos["chave"]  # KeyError`

`contatos.get("chave")  # None`

`contatos.get("chave", {})  # {}`

`contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome":"Guilherme", "telefone": "3333-2221"}`

**{}.items**

O método **items** retorna todos os valores do dicionario e as chaves

**exe:**

`contatos = {`

    `"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}`
    
`}`

`contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])`

**{}.keys**

O método **keys** retorna todos os valores das chaves somente

**exe:**
`contatos = {`

    `"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}`
    
`}`

`contatos.keys()  # dict_keys(['guilherme@gmail.com'])`

**{}.pop**

O método **pop** remove um valor do dicionário e retorna esse valor se caso ele for encontrado

**exe:**

`contatos = {`

   `"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}`
   
`}`

`contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}`

`contatos.pop("guilherme@gmail.com", {})  # {}`

**{}.popitem**

O método **popitem** remove os items de um dicionário na sequencia

**exe:**

`contatos = {`

     `"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}`
`}`

`contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})`

`contatos.popitem()  # KeyError`

**{}.setdefault**

O método **setdefault** se caso o valor de chave ja existir ele não adiciona, caso contrário ele adiciona a chave com o seu valor.

**exe:**

``contato = {'nome': 'Guilherme', 'telefone': '3333-2221'}`

`contato.setdefault("nome", "Giovanna")  # "Guilherme"`

`contato  # {'nome': 'Guilherme', 'telefone': '3333-2221'}`

`contato.setdefault("idade", 28)  # 28`

`contato  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}`

**{}.update**

O método **update** permite que o dicionário seja atualizado com outros dicionários.

**exe:**

`contatos = {`

   `"guilherme@gmail.com": {"nome": "Guilherme","telefone": "3333-2221"}`
   
`}`

`contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})`

`contatos  # {'guilherme@gmail.com': {'nome': 'Gui'}}`

`contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})`

`contatos  # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}`

**{}.values**

O método **values** retorna todos os valores do dicionário.

**exe:**

`contatos = {`

    `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},`
    
    `"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},`
    
    `"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},`
    
    `"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},`
`}`

`contatos.values()  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])`

**in**

O método **in** verifica se um determinado valor é uma chave em um determinado dicionário.

**exe:**
`contatos = {`

   `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},`
   
   `"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},`
   
   `"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},`
   
   `"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},`
   
`}`

`"guilherme@gmail.com" in contatos  # True`

`"megui@gmail.com" in contatos  # False`

`"idade" in contatos["guilherme@gmail.com"]  # False`

`"telefone" in contatos["giovanna@gmail.com"]  # True`

**del**

O método **del** apaga valores do dicionário

**exe:**

`contatos = {`

    `"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},`
    
    `"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},`
    
    `"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},`
    
    `"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},`
`}`

`del contatos["guilherme@gmail.com"]["telefone"]`

`del contatos["chappie@gmail.com"] `

`contatos # {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': 3443-2121'},`'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}`

# Curso 10: Dominando Funções em Python 🐍 📝
## Dominando Funções Python
### Funções Python - Parte 01
### Funções Python - Parte 02



















