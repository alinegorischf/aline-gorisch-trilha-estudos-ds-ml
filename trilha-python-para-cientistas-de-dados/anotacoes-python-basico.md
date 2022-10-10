# Anotações aulas :memo:

## Curso: Ambiente de Desenvolvimento e Primeiros Passos com Python :snake:

### Definindo o ambiente e primeiros passos com Python

**Introdução ao Python**

Python foi criada em 1989 pelo programador Guido Van Rossum. A ideia era dar continuidade a linguagem ABC desenvolvida no Centro de Pesquisa Holandês (CWI), essa era uma linguagem pensada para iniciantes devido a sua facilidade de aprendizagem e utilização. Ele quis continuar o projeto  como hobby  e seus objetivos para a linguagem Python eram:

* Uma linguagem fácil e intuitiva
* Código aberto, para que todos possam contribuir
* Código tão inteligível quanto o inglês.
* Adequadas para tarefas diárias, e produtiva!

**Linha do tempo do Python**

1989 - 1991: Guido Van Rossum inicia o desenvolvimento em 1989 e em 1991 lança a primeira versão pública (0.9.0).

1994: É lançada a versão 1.0 do Python

1995: Guido lança a versão 1.2 e encerra seu vínculo no centro de pesquisa CWI, criando então a **BeOpen Python Labs** (BeOpen.com) junto com a equipe dos principais desenvolvedores Python. 

2000 - 2001 : A segunda versão de Python é publicada junto com essa versão nasce a **List Comprehensions**. Em 2001 nasce a Python Software Foundation (PSF),  com isso a partir do Python 2.1 todo o código possui documentação e especificações de linguagem.

2008: É lançada a versão 3.0 com melhor performance e problemas de design solucionados, com isso mudanças profundas foram feitas fazendo com que o Python versão 3 não fosse retrocompatível (um código escrito em python 2 não roda em python bem como o contrário).

**Por quê?**

Python é uma linguagem versátil e possui as seguintes características:

* Tipagem dinâmica e forte (não é necessário definir o tipo da entrada ou dado : int, float)
* Multiplataforma e multiparadgima. (roda em linux, windows e etc... suporta vários paradigmas de programação: orientação a objetos, programação procedural e etc.. )
* Comunidade expressiva e ativa.
* Curva de aprendizado baixa. (fácil de aprender para quem está iniciando e fácil de se adaptar para quem já tem experiência).
* **Não** é recomendado para Mobile

**Configuração de ambiente de desenvolvimento**

link instalação Windows: http://python.org.br/instalacao-windows/

*python --version*: comando do terminal do windows  para ver se o Python está instalado

**IDE recomendada pelo prof**

**VSCode** pelos seguintes motivos: é gratuita, suporta múltiplas tecnologias e tem boa performance

No VsCode instalar as extensões: Python, autoDocstring e intelliCode

## Curso: Conhecendo a Linguagem de Programação Python :snake:

### Tipos de Dados

Os tipos de dados servem para definir as características  e os comportamentos de um valor (objeto) para o interpretador, ou seja o número (objeto) 10 é do tipo int e com ele eu consigo realizar operações matemáticas, outra caracterista é em relação ao armazenamento ou seja quanto de memória esse objeto irá consumir.

Os tipos padrões da linguagem são:

* Texto: str 
* Númerico: int , float , complex 
* Sequência: list, tupla, range
* Mapa: dict
* Coleção: set, fronzenset
* Booleano: bool
* Binário: bytes, betearray, memoryview

**Tipos de números**

Números inteiros:

São representados pela classe **int** e possuem precisão limitada. exe: 1,10,100,-1,-10,-100...

Números de ponto flutuante:

São usados para representar os números racionais e sua implementação é feita pela classe **float**. exe: 1.5, -10.543, 7.76...

Booleanos:

É usado para representar verdadeiro ou falso, e é representado pela classe **bool**. Em Python o tipo booleano é uma subclasse de **int**, uma vez que qualquer número diferente de 0 representa verdadeiro (true) e 0 falso (false).

**Strings**

São usadas para representar valores alfanuméricos, em Python as string são definidas utilizando a classe **str**. exe: "python", 'p', ""Python"".....

**Tipos de Dados representados no Python**

*int*: `print(11 + 1000)` = 1011

*float*: `print(1.5 + 1 +0.5)` = 3.0

*booleano*: 

`print(True) ` = True 

`print(False)` = False

*str*: `print('Python')` = Python

**Tipos de classes (construtores) no Python**

**int**()

**float**()

**bool**()

**str**()

### Modo Interativo

O interpretador Python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na hora. E isso pode ser feito de duas maneiras: 1ª escrevendo (python) no terminal ou 2ª executando o script com a flag -i (python -i app.py). exe:

entrada: `>>> 1 + 10`

saída: 11

entrada: `python -i Primeiro-programa.py`

saída: Olá, mundo!

**Funções dir e help**

**dir**

Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto

sem argumentos: 

entrada: `>>> dir()`

saída: ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

com argumentos:

entrada: `>>> dir(100)`

saída: ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

**help**

Invoca o sistema de ajuda integrado (documentação). É possível em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável. Exemplo:

sem argumento: `>>> help()`

saída: permite pesquisa, exemplo: int ele retorna todos metódos.

com argumento: `>>> help(100)`

saída: retorna a classe, métodos...

### Variáveis e constantes

**Variáveis**

Em linguagens de programação podemos definir valores que podem sofrer alterações a medida que executamos o programa. Esses valores recebem o nome de variáveis, pois nascem com um valor e não necessariamente devem permanecer com o mesmo valor ao longo da execução do programa.

**Alteração de valores**

Não é necessário atribuir o tipo de dado da variável, o Python faz isso automaticamente através do seu interpretador. Por isso não podemos criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma atribuição de um novo valor.

**Constantes**

São utilizadas para armazenar valores, porém o valor de uma constante se mantém o mesmo até o final da execução do programa, fazendo dele um valor imutável.

**Python não tem constantes**

Não existe uma palavra reservada para informar ao interpretador que o valor é uma constante. Por isso em Python usa-se a convenção que a variável é uma constante. Para fazer isso, deve-se criar a variável com o nome todo em letras maiúsculas.

**Boas práticas**

* O padrão de nome deve ser snake case. (não deixar espaços em branco usar o _)
* Escolher nomes sugestivos. (que façam sentido pro teu programa)
* Nome de constantes todo em maíusculo

### Conversão de tipos

**Convertendo tipos**

Em alguns momento será necessário converter o tipo de uma variável para manipular de forma diferente. Por exemplo:

Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.  

**Conversão inteiro para float**

`preco = 10
print(preco)`

`preco = float(preco)
print(preco)`

**Conversão float para inteiro**

`preco = 10.30
print(preco)`

`preco = int(preco)
print(preco)`

**Conversão por divisão**

`preco = 10
print(preco)`

**Converter inteiro para número float**

`print(preco / 2)`

**Converter float para número inteiro**

`print(preco // 2)`

**Converter número para string**

`preco = 10.50
idade = 28`

`print(str(preco))`

`print(str(idade))`

`texto = f"idade {idade}, preco {preco}"`

`print(texto)`

**String para número**

`preco = "10.50"
idade = "28"`

`print(float(preco))`

`print(int(idade))`

### Funções de entrada e saída

**Função *input***

A função *input* é utilizada quando queremos ler dados de entrada padrão (teclado). Ela recebe um argumento do tipo string,  que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

`nome = input("Informe seu nome: ")`

**Função print**

A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end, A string final é exibida para o usuário.

`nome = "João"
sobrenome = "Andrade"`

`print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")`

`>>>João Andrade
´>>>João Andrade
´>>>João#Andrade`

## Curso: Tipo de operadores :snake:

### Operadores Aritméticos

**Conhecendo os operadores aritméticos**

Os operadores aritméticos executam operações matemáticas, como adição, subtração com operandos. Exe..

**Variáveis**

``produto_1 = 20
produto_2 = 10`

**Adição**

`print(produto_1 + produto_2)`

= 30

**Subtração**

`print(produto_1 - produto_2)`

= 10

**Divisão**

`print(produto_1 / produto_2)`

= 2.0

**Divisão inteira**

`print(produto_1 // produto_2)`

= 2

**Multiplicação**

`print(produto_1 * produto_2)`

= 200

**Exponenciação**

`print(produto_1 ** produto_2)`

= 10240000000000

**Módulo é o resto da divisão**

`print(produto_1 % produto_2)`

= 0 

**Precedência dos operadores**

Na matemática existe uma regra que indica quais operações devem ser executadas primeiro. Isso é útil pois ao analisar uma expressão os valores podem mudar dependendo da ordem das operações.

 x = 10 - 5 * 2

x é igual a 0 ou 10?

x = 10 - ( 5 * 2 )

x = 0

A definição indica a seguinte ordem como a correta:

* Parêntesis
* Expoentes
* Multiplicações de divisões (da esquerda para a direita)
* Somas e subtrações (da esquerda para a direita)

### Operadores de comparação

São operadores utilizados para comparar dois valores

**Variáveis**

`saldo = 200
saque = 200`

**Igualdade**

`print(saldo == saque)`

= True

**Diferença**

`print(saldo != saque)`

= False

**Maior que / maior ou igual**

`print(saldo > saque)
print(saldo >= saque)`

= False

= True

**Menor que / menor ou igual**

`print(saldo < saque)
print(saldo <= saque)`

= False

= True

### Operadores de atribuição

São operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variável

**Atribuição simples**

`saldo = 200
print(saldo)`

= 200

**Atribuição com adição**

`saldo += 10
print(saldo)`

= 210

**Atribuição com subtração**

`saldo -= 5
print(saldo)`

= 205

**Atribuição com divisão inteira**

`saldo //= 2
print(saldo)`

= 102

**Atribuição com divisão**

`saldo /= 2
print(saldo)`

= 51.0

**Atribuição com multiplicação**

`saldo *= 10
print(saldo)`

= 510.0

**Atribuição com módulo**

`saldo %= 4
print(saldo)`

= 2.0

**Atribuição com exponenciação**

`saldo **= 2
print(saldo)`

= 4.0

### Operadores lógicos

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:

op_comparacao_ + op_logico + op_comparacao...N...

**Operador E (para ser verdadeiro é necessário que TODAS as operações sejam verdadeiras e para ser falso é necessário que apenas UMA das operações sejam falsas)**

`print(True and True and True)
print(True and False and True)
print(False and False and False)`

= True

= False

= False

**Operador OU (para ser verdadeiro é necessário que UMA das operações sejam verdadeiras e para ser falso é necessário que TODAS as operações sejam falsas) **

`print(True or True or True)
print(True or False or False)
print(False or False or False)`

= True

= True

= False

**Exemplo**

`saldo = 1000
saque = 250
limite = 200`
`conta_especial = True`

`exp_1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp_1)`

`exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)`

`= True
= True`

**Boas práticas para construção de operadores de comparação **

`conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque`

`exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente`

`print(exp_3)`

`= True`

**Obs:**

Operador de negação (a negação de falso é verdadeiro e a negação de verdadeiro é falso)

Parênteses (os parênteses servem para delimitar a precedência da execução de comparação entre operações lógicas ).

### Operadores de identidade

São operadores utilizados para comparar se dois objetos testados ocupam a mesma posição na memória.

`saldo = 1000
limite = 500`

`print( saldo is limite)
print(saldo is not limite)`

`= True
= False`

`saldo = 1000
limite = 1000`

`print( saldo is limite)
print(saldo is not limite)`

`= True
= False`

### Operadores de associação

São operadores utilizados para verificar se um objeto está presente em uma sequência. 

**Exemplos**

`frutas = ["limao", "uva"]
curso = "Curso de Python"`

Para verificar se um objeto **está** presente

`print("laranja" in frutas)
print("Python" in curso)`

`= False
= True`

Para verificar se um objeto **não está** presente

`print("limao" not in frutas)
print("Java" not in curso)`

`= False
= True`

**REFERÊNCIAS**

https://docs.python.org/3/library/stdtypes.html

https://wiki.python.org.br/ModoInterativohttps://docs.python.org/3/library/functions.html#input

https://docs.python.org/3/library/functions.html#print

## Curso: Estruturas condicionais e de repetição :snake:

### Indentação e blocos

**A estética**

Indentar código é uma forma de manter o código fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.

 **Bloco de comando**

As linguagens de programação costumam utilizar caracteres ou palavras reservados para determinar o início e fim do bloco. 

**Utilizando espaços**

Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja a cada novo bloco adicionamos 4 novos esoaços.

`def sacar(valor):
    saldo = 500`

    if saldo >= valor:
        print("Valor sacado")
        print("retire o dinheiro na boca do caixa")
    
    print("Obrigado por ser nosso cliente!")

`sacar(10)`

### Estruturas condicionais

A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

**if**

Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada **if**. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

`MAIOR_IDADE = 18
    idade = int(input("Informe sua idade: "))`

    if idade >= 18:
        print("Maior de idade, pode tirar a CNH.")
        
    if idade < 18:
        print("Ainda não pode tirar CNH.")   

**if / else**

Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas **if** e **else**. Como sabemos se a expressão lígica testada no **if** for verdadeira, então o bloco de código do **if** será executado. Caso contrário o bloco de código **else** será executado

`MAIOR_IDADE = 18
    idade = int(input("Informe sua idade: "))`

    if idade >= 18:
        print("Maior de idade, pode tirar a CNH.")
        
    else:
        print("Ainda não pode tirar CNH.")   

**if / elif / else**

Em alguns casos queremos mais que dois desvios, para isso podemos utilizar a palavra reservada **elif**. O **elif** é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do **elif** será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexidade do código.

`MAIOR_IDADE = 18
 IDADE_ESPECIAL = 17`

`idade = int(input("Informe sua idade: "))`

    if idade >= 18:
        print("Maior de idade, pode tirar a CNH.")
        
    elif idade == IDADE_ESPECIAL:
        print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
        
    else:
        print("Ainda não pode tirar CNH.") 

**Estrutura condicional aninhada (if aninhado)**

Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas uf/elif/else dentro do bloco de código de estruturas if/elif/else.

`conta_normal = False
conta_universitária = False
conta_especial = True`

`saldo = 2000
saque = 1500
cheque_especial = 450`

    if conta_normal:
    
        if saldo >= saque:
            print("Saque realizado com sucesso!")
    
        elif saque <= (saldo + cheque_especial):
            print("Saque realizado com uso do cheque especial!")
    
        else: 
            print("Não foi possível realizar o saque, saldo insuficiente!")
    
    elif conta_universitária:
    
        if saldo >= saque:
            print("Saque realizado com sucesso!")
    
        else:
            print("Saldo insuficiente!")
        
    elif conta_especial:
            print("Conta especial selecionada!")
    
    else:
        print("Sistema não reconheceu seu tipo de conta, entre em contato com seu gerente!")

**Estrutura condicional  (if ternário)**

O **if** ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso e a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

`saldo = 2000
saque = 1500`

    status = "Sucesso" if saldo >= saque else "Falha"
    
    print(f"{status} ao realizar o saque!")

### Estruturas de repetição

São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse numero pode ser conhecido previamente ou determinado através de uma expressão lógica.

 **Estruturas de repetição Comando for **

O comando for é usado para percorrer um objeto iterável. Faz sentido usar quando sabemos o número exato de vezes que nosso bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável.

`texto = input("Informe um texto: ")
VOGAIS = "AEIOU"`

    for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="")
    
    print() # adiciona uma quebra de linha

**Estruturas de repetição Comando for / else**

exe: utilizando um iterável

`texto = input("Informe um texto: ")
VOGAIS = "AEIOU"`

    for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="")
            
    else:
    	print() # adiciona uma quebra de linha
    	print("Executa no final do laço")

**Estruturas de repetição Função range**

Range é uma função built-in do Python, ela é usada para produzir uma sequencia de números inteiros a partir de um início (inclusivo) para um fim (exclusivo). Se usarmos (i, j) será produzido:

i, i+1, i+2, i+3....., j+1.

Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step opcional.

exe: utilizando a função built-in range

`for numero in range(0, 51, 5):
    print(numero, end=" ")`

**Estruturas de repetição Comando while**

O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.

exe: utilizando a função while

`opcao = -1`

    while opcao != 0:
        opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n: "))
    
        if opcao == 1:
            print("Sacando...")
    
        elif opcao == 2:
            print("Exibindo o extrato...")

exe: utilizando a função while / else

`opcao = -1`

    while opcao != 0:
        opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair\n: "))
    
        if opcao == 1:
            print("Sacando...")
    
        elif opcao == 2:
            print("Exibindo o extrato...")
    else:
        print("Obrigado por usar nosso sistema bancário, até logo!")

**Estruturas de repetição Comando Break**

Ele para o laço de repetição no momento em que a condição for atendida

    while True:
        numero = int(input("Informe um número: "))
        
        if numero == 10:
           break
    
        print(numero)
    
    for numero in range(100):
    
        if numero == 15:
          break
    
        print(numero, end=" ")

**Estruturas de repetição Comando Continue**

Ele pula a execução 

    for numero in range(100):
    
        if numero % 2 == 0:
            continue
    
        print(numero, end=" ")

**Estruturas de repetição Comando Break e Continue no while**

    while True:
        numero = int(input("Informe um número: "))
    
        if numero == 10:
            break
        if numero % 2 == 0:
            continue
         
        print(numero)

## Curso: Dominando Strings e Fatiamento :snake:

### Conhecendo métodos úteis da classe string

A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar. 

Em algumas linguagens manipular sequencias de caracteres não é um trabalho trivial, porém, em python esse trabalho é muito simples.

**Maiúscula, minúscula e título**

exemplo: "PytHon"

Maiúscula

print(nome.upper())

= PYTHON

Minúscula

print(nome.lower())

= python

Título

print(nome.title())

= Python

**Eliminando espaços em branco**

exemplo: 

nome = "	Python  "

Remover espaço em branco da esquerda e da direita

print(nome.strip())

= Python

Remover espaço em branco da esquerda

print(nome.lstrip())

= "Python  "

Remover espaço em branco da direita

print(nome.rstrip())

= "	Python"

**Junções e centralização**

Centralizado: é necessário colocar o argumento de quantos números vc deseja colocar que pode ser o número de caracteres da variável + quantos números desejar o segundo argumento é opcional se não for preenchido o valor irá retornar com espaço em branco.

print(nome.center(10, "#")) ou print(nome.center(10))

​          = "##Python##"             ou        = "   Python   "    

Junções: é necessário colocar como argumento o caractere que será adicionado a string (é mais comum em listas)

print( " . " . join(curso))

= "P.y.t.h.o.n"

### Interpolação de variáveis

Há duas forma recomendadas de interpolar variáveis em string, a primeira é utilizando o método **format** e a segunda é utilizando  o **f strings**

**Método Old style % (não é recomendado o uso**

    nome = "Aline"
    idade = 31
    
    saldo = 45.435
    
    dados = {"nome": "Aline", "idade": 31}
    
    Old Style %
    # print("Nome: %s Idade: %d" % (nome, idade))
    
    # Método Formta
    # print("Nome: {} Idade: {}".format(nome, idade))
    # print("Nome: {0} Idade: {1}".format(nome, idade))
    # print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
    # print("Nome: {nome} Idade: {idade}".format(**dados))
    
    # Método f strings
    print(f"Nome: {nome} Idade: {idade} saldo: {saldo:.2f}")

**Método format**

    nome = "Aline"
    idade = 31
    
    dados = {"nome": "Aline", "idade": 31}
    
     Método Formta
     print("Nome: {} Idade: {}".format(nome, idade))
     print("Nome: {0} Idade: {1}".format(nome, idade))
     print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
     print("Nome: {nome} Idade: {idade}".format(**dados))

**Método f strings (melhores práticas)**

    nome = "Aline"
    idade = 31
    profissao = "Geógrafa"
    linguagem = "Python"
    
    saldo = 45.435
    
    # Método f strings
    print(f"Nome: {nome} Idade: {idade} saldo: {saldo:.2f}")

### Fatiamento de string

Fatiamento de string é uma técnica utilizada para retornar substrings (partes da string original), informando inicio (start), fim (stop) e passo (step): [start: stop[, step]].

    nome = "Aline Gorisch Ferreira"
    
    print(nome[0])
    print(nome[:6])
    print(nome[6:22])
    print(nome[0:14:2])
    print(nome[::-1])
    print(nome[-1])

### strings (triplas) múltiplas linhas

Strings de múltiplas linhas são definidas informados 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.

    nome = "Aline"
    
    mensagem = f'''
    Olá meu nome é {nome},
    estou aprendendo python
    '''
    print(mensagem)
    
    mensagem = f"""
    	Olá meu nome é {nome},
    estou aprendendo python
    """
    print(mensagem)
