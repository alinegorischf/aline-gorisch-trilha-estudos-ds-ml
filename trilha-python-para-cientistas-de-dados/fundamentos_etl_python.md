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


