# Curso: Fundamentos de ETL (Extract, Transform, Load) com Python :card_file_box:

Nível: Intermediário

Carga horária: 2h

Skills: Python, Data

## Fundamentos de ETL

### Introdução para ETL
ETL é um tipo de **data integration** em três etapas **(extração, transformação e carregamento)** usado para combinar dados de diversas fontes. 
Ele é comumento utilizado para construir um **data warehouse**
![image](https://user-images.githubusercontent.com/112986146/197031006-56933c97-58af-4230-9562-81b8e4ff0d49.png)

![image](https://user-images.githubusercontent.com/112986146/197031238-998568c2-219b-466c-85d5-413ab4c21203.png)

ETLs, são ferramentas de software cuja função é a extração de dados de diversos sistemas, transformação desses dados conforme regras de negócios 
e por fim o carregamento dos dados geralmente para um Data Mart e/ou Data Warehouse. 

Nesse processo, os dados são retirados (extraídos) de um sistema-fonte, convertidos (transformados) em um formato que possa ser analisado, e 
armazenados (carregados) em nuvem ou outro sistema. Extração, carregamento, transformação (ELT) é uma abordagem alternativa, embora relacionada,
projetada para jogar o processamento para o banco de dados, de modo a aprimorar a performance.
![image](https://user-images.githubusercontent.com/112986146/197031817-3ff1b613-f040-48d6-9bc4-02ec655219b5.png)

**Ferramentas**
Existem muitas ferramentas de ETL disponíveis no mercado como: **IBM Information Server (Data Stage), o Oracle Data Integrator (ODI), 
o Informatica Power Center, o Microsoft Integration Services (SSIS)**. Existe também um conjunto de Ferramentas de ETL Open Source como o PDI – 
Pentaho Data Integrator e Talend ETL.

O processo de extração, transformação e carregamento (ETL) abrange alguns passos importantes. Como exemplo, podemos considerar 
um Banco de dados de Clientes Especiais com todas as informações essenciais.
No mapeamento, a extração de origem deve conter a especificação da identidade e seus atributos detalhados, tudo armazenado numa zona 
temporária.

Quando forem efetuadas as análises e filtragens dos dados, a nova versão poderá ser comparada com a cópia da versão prévia!
A transformação inclui limpeza, racionalização e complementação dos registros. O processo de limpeza removerá erros e padronizará as 
informações. O processo de complementação implicará no acréscimo de dados.

### Etapas para ETL
**1. Extract**

O **processo de Extração de dados** consiste em se comunicar com outros sistemas ou bancos de dados para capturar os dados que serão 
inseridos no destino, seja uma Staging Area ou outro sistema.

**2. Transform**

O processo de **Transformação de Dados** é composto por várias etapas : padronização, limpeza, qualidade. Dados vindos de sistemas diferentes 
tem padrões diferentes seja de nomenclatura ou mesmo de tipos de dados ( VARCHAR2 Oracle ou VARCHAR Sql Server.

**3. Load**

O **processo de Load** é a etapa final onde os dados são lidos das áreas de staging e preparação de dados, carregados no Data Warehouse ou 
Data Mart Final.

![image](https://user-images.githubusercontent.com/112986146/197032660-ca7243c4-d8ed-4483-b172-5b6f24544cec.png)

#### Vantagens do ETL
**Garantia significativa da qualidade dos dados**

A Ferramentas de ETL, através de sequências de operações e instruções tem condições de solucionar problemas de maior complexidade.

**Funcionalidade de execução**

Uma ferramenta de ETL já possui suas funções específicas, sendo necessária apenas a atenção no fluxo de dados.

**Desenvolvimento das cargas**

Mesmo que o usuário não seja técnico poderá desenvolver uma rotina de carga em uma ferramenta de ETL, devido a facilidade 
e rapidez para codificação.

**Manutenção das cargas**

As tarefas de manutenção de uma rotina de carga são mais simples de realizar em relação à manutenção de código.

**Metainformação**,

Os metadados (informações úteis para identificar, localizar, entender e gerenciar os dados) são gerados e mantidos de forma automática 
com a ferramenta, evitando problemas de geração de informações incorretas na finalização do processo.

**Performance**

Os métodos mais usados para trabalhar com grandes volumes conseguem extrair, transformar e carregar dados com maior 
velocidade e menos recursos, como gravações em bloco e operações não logadas.

**Transferência**

Ferramentas de ETL podem ser deslocadas de um servidor mais facilmente ou distribuídas entre vários servidores.

**Conectividade**

A conexão de uma ferramenta de ETL com múltiplas fontes de dados é transparente. Caso sejam precisas mais fontes como o SAP, VSAM, 
Mainframe ou qualquer outra, basta a aquisição do conector sem a necessidade de codificar um.

**Reinicialização**

Ferramentas possuem a capacidade de reiniciar a carga de onde pararam sem a necessidade de codificação.

**Segurança e Estabilidade**

É possível articular melhor a segurança tornado-a mais modular, dividindo as finalidades 
(criação de cargas, execução de cargas, agendamento, etc.)

### Ferramenta aplicadas para ETL
**Ferramentas utlizadas**

As ferramentas são softwares **utilizados para facilitar o processo de integração de dados**. Inicialmente muito usados em projetos de **Data Warehouse e Business Inteligence** em geral, ultimamente tem sido utilizados em processo de integração de softeare, banco de dados, etc.
![image](https://user-images.githubusercontent.com/112986146/197197537-6fdec43f-1367-4d70-aee3-6d66bea78077.png)

**Existem diversas ferramentas de ETL, como:**

**IBM Data Stage** - https://www.cetax.com.br/datastage-ibm-ferramenta-de-etl/

**Power Center** - https://www.cetax.com.br/power-center-informatica-ferramenta-de-etl/

**SQL Server Integration Services** - https://www.cetax.com.br/ssis-sql-server-integration-Talend

**Talend ETL** - https://www.cetax.com.br/criando-job-simples-no-talend/
![image](https://user-images.githubusercontent.com/112986146/197198256-1257a7e6-c779-4aaf-a078-d503fb29b9a3.png)

**ETL para Big Data**

Hoje com o crescimento dos projetos de Big Data aumenta-se mais ainda a necessidade de fazer ETL entre plataformas heterogêneas, para isso, projetos como o Hadoop, posuem ferramentas próprias para carga de dados, como:

**SQOOP** - Ferramenta para movimentar dados entre banco de dados relacionais e o ambiente Hadoop.

**HIVE** - Ambiente SQL sobre um cluster Hadoop.

**PIG** - Ferramenta de Script para transformação e processamento de dados.

**SPARK** - Framework de processamento em memória.

**O que é Hadoop**

Hadoop é uma plataforma de software em Java de computação distribuída voltada para clusters e processamento de grandes volumes de dados, com atenção a tolêrancia a falhas.

Mesmo com todas as possibilidades acima, vemos as ferramentas de ETL se adaptando para **Big Data** ou gerando códigos para serem rodados nessas ferramentas do Ecossistema Hadoop.

Em Big Data, o processo de carga também é conhecido como ingestão de Dados, que geralmente é a primeira parte de carga (Extract) a parte mais simples do processo, que consiste em Extrair dados dos sistemas de origem e trazer para dentro do Data Lake ou ambiente de dados utilizados.

### Introdução à biblioteca Pandas
**Utilizando a biblioteca**

O pandas permite trabalhar com diferentes tipos de dados, por exemplo:

* Dados tabulares, como planilha do excel ou uma tabela SQL;
* Dados ordenados de modo temporal ou não, Matrizes;
* Qualquer conjunto de dados, que não necessariamente precisem estar rotulados;

**Bibliotecas de exemplo:**

* [OpenCV](https://docs.opencv.org/4.x/index.html)
* [pillow](https://pillow.readthedocs.io/en/stable/)
* [scikit-image](https://scikit-image.org/)

**Estruturas de Dados**

* Os dois principais objetos da biblioteca Pandas são as **Series** e os **DataFrames**
* Uma [Série](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series) é uma matriz unidimensional que contém uma sequencia de valores que apresentam uma indexação (que podem ser numéricos ou inteiros ou rótulos), muito parecida com uma única coluna no Excel.
* Já o [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) é uma estrutura de dados tabular, semelhante a planilha de dados do Excel, em que tanto as lihas quanto as colunas apresentam rótulos.

![image](https://user-images.githubusercontent.com/112986146/197341456-b518b67b-3343-4e07-9a45-24c99ccac169.png)

As vantagens são [comandos equivalentes](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/index.html), com a mesma funcionalidade no Pandas;
![image](https://user-images.githubusercontent.com/112986146/197341557-4cef4232-a1c6-413b-b14f-6351f1114908.png)

### Biblioteca Pandas e suas funções

**DataFrame**

Agora se visualizarmos novamente os primeiros 4 dados do nosso conjunto, veremos que todos os valores passados para na_values, além dos próprios dados ausentes, foram substituídos por NaN.
![image](https://user-images.githubusercontent.com/112986146/197342143-63fca6eb-5390-4b38-a0f3-546feac66148.png)

**df.shape**

Essa função permite a vizualização do tamanho do nosso conjunto de dados, neste caso seriam 549 linhas e 7 colunas.
![image](https://user-images.githubusercontent.com/112986146/197342197-ce0eae5d-ca3f-4210-bbd5-c4f39b4f02f3.png)

**df.info**

Essa função retorna aa informações relacionadas em cada coluna, além da quantidade de memória para ler esse conjunto de dados, podemos utilizar o comando info:
![image](https://user-images.githubusercontent.com/112986146/197343250-3e6d89dd-44d3-496d-a6df-0952e181d48c.png)

**Alterações**

Na sequência, podemos visualizar quais são nossas colunas existentes e até mesmo alterar esses nomes, basta passar o novo conjunto de nomes desejados com a mesma quantidade de colunas existente no conjunto original:
![image](https://user-images.githubusercontent.com/112986146/197343274-26cc5bf5-0869-47d3-a170-b7c3bc37feee.png)

**Verificação**

Para verificar quantos dados faltantes existem em nosso conjunto
![image](https://user-images.githubusercontent.com/112986146/197343301-67c2a850-cdb3-4223-a1d3-c76906548300.png)

**Valores únicos**

No nosso objeto Serie podemos verificar quais os valores únicos existem naquela coluna, com o método unique:
![image](https://user-images.githubusercontent.com/112986146/197343326-1ec40abe-a953-42b0-9e41-7cf2157e5797.png)

**Agrupamentos**

Ainda a partir desse método podemos gerar uma visualização simples e rápida com o resultado. Como? Com o método plot.
![image](https://user-images.githubusercontent.com/112986146/197343353-9da9d33d-e986-4359-8299-b9f8ace432ac.png)

**Dados estatísticos**

O Pandas colabora na exibição de algumas informações estatísticas a respeito do nosso conjunto de dados e permite que possamos realizar facilmente uma análise com o nosso objeto DataFrame
![image](https://user-images.githubusercontent.com/112986146/197343380-1d661ace-683b-4774-b986-d71a1ba8921f.png)

### Introdução à biblioteca Scikit Learn

**Utilizando a biblioteca**

Esta biblioteca dispõe de ferramentas simples e eficientes para análise preditivas de dados, é reutilizável em diferentes situações, possui código aberto, sendo acessível a todos e foi construída sobre os pacotes **NumPy, SciPy, matplotilib.**

Neste exemplo iremos criar uma massa de dados com 200 observações, com apenas uma variável preditora, que será a variável x e a variável target, que será a y. Para isso indicamos os parâmetros n_samples = 200 e n_features = 1. O parâmetro noise define o quão dispersos os dados estarão um dos outros. 

from sklearn.datasets import make_regression

gerando uma massa de dados:

x, y = make_regression(n_samples=200, n_features=1, noise=30).

![image](https://user-images.githubusercontent.com/112986146/197345524-9861c3a6-0369-481b-a9c8-7b5bc29ba6ef.png)

Utilizaremos o pacote matplotlib, com o módulo pyplot e a função scatter(), que criará o gráfico, e função show() que o exibirá na tela.!

![image](https://user-images.githubusercontent.com/112986146/197345544-c246414e-d0cc-4ef5-a19e-c871e7f8ed05.png)

Com os dados gerados, já podemos iniciar a criação de nosso modelo de machine learning. Para isso utilizaremos o módulo linear_model, e a função LinearRegression().

from sklearn.linear_model import LinearRegression

Criação do modelo

modelo = LinearRegression()

Após esta execução, o objeto modelo que acabamos de criar está pronto para receber os dados que darão origem ao modelo. Como não indicamos nenhum parâmetro específico na função, estamos utilizando suas configurações padrão.

Agora precisamos apenas apresentar os dados ao modelo, e para isso temos o método fit().Na documentação da função podemos conferir todos os métodos que ela possui.

Após esta etapa, nosso modelo de machine learning está pronto e podemos utilizá-lo para prever dados desconhecidos. Simplificando este primeiro entendimento, vamos apenas visualizar a reta de regressão linear que o modelo gera, com os mesmos dados que criaram o modelo. Para isso iremos utilizar o método predict(), indicando que queremos aplicar a previsão nos valores de x.  O resultado do método será uma previsão de y para cada valor de x apresentado.

![image](https://user-images.githubusercontent.com/112986146/197345638-570f688d-c315-4f34-bb57-2faaf5c728ee.png)

A função plot() do pacote pyplot gera uma reta com os dados apresentados. Como já temos os dados de x e y, basta indicá-los na função. Assim, primeiramente montamos novamente o gráfico de x e y original com a função scatter(), e somamos a ele a reta de 

![image](https://user-images.githubusercontent.com/112986146/197345665-267ba250-3a4a-430b-851e-c38030c34802.png)



