# Anotações curso Fundamentos de ETL com Python

Informações do curso:
Aprenda sobre o processo de Extract Transform and Load (ETL) e como transformar seus dados e deixa-los prontos para seus projetos.

Nível: Básico

Carga horária: 5h

Skills: Python, Data

## Fundamentos ETL

### Introdução ao ETL - Definição
**Objetivos**

1- Definição

2- Por que precisamos

3- Visão geral

4- Algumas ferramentas e pacotes

5- Para saber mais

### Definição
O processo de ETL percorre 3 etapas

1)**Extract:** os dados são extraídos de diferentes fontes de dados.

2)**transform:** Propagados para a área de preparação de dados, onde são transformados e limpos.

3)**Load:** Carregados no data warehouse.

### Por que precisamos?
O ETL é uma etapa de extrema importância na tomada de decisões. Como os dados podem vir de fontes e extensões diferentes, a tomada de decisão com esses dados brutos se torna algo impossível, por isso é necessário a etapa do ETL, pois nesse processo é que todos os dados serão **estraídos** de acordo com o contexto do projeto e existem duas formas de extração, em lote **(Batch)** essas extrações devem ocorrem em momentos específicos, devido a complexidade e tamanho o que pode fazer com que outros setores não operem de forma produtiva, sendo recomendado planejar a extração quando houver menos quantidade de trabalho ou em períodos noturnos. E dados que podem ser processados em tempos real **(Real Time)**. Após a extração os dados dvem ser **transformados**, para sem seguida serem **validados**, **normalizados** e carregados de forma integra e dentro do contexto de negócio. Após esse processo os dados podem ser relacionados e ferramentas de visualização podem ser usadas e relacionadas com esses dados.

### Visão geral sobre ETL

**Data Sources**: Diferentes fontes de dados, que armazenam os dados que vão ser extraídos e carregados para dentro do contexto da empresa.

**Data Flow / pipeline**: Data Flow caminhos dos dados até o carregamento e disponibilidade para visualização (Data validation, data cleaning, Data transforming, Data agregation, Data loading) Pipeline segimentação dos processos (Datamarts).

**BI results**: (OLAP Analisys, Data Mining, Data Visualization, Reports, Dashboards e Alerts)

### Ferramentas e Pacotes
**Ferrmentas e Pacotes para a lingugem Python**

* **Apache Airflow**: O Apache Airflow é uma plataforma de código aberto para desenvolvimento, agendamento e monitoramento de fluxos de trabalho orientados a lotes. A estrutura Python extensível do Airflow permite que você crie fluxos de trabalho conectando-se a praticamente qualquer tecnologia. Uma interface da Web ajuda a gerenciar o estado de seus fluxos de trabalho. O Airflow pode ser implantado de várias maneiras, variando de um único processo em seu laptop a uma configuração distribuída para oferecer suporte até mesmo aos maiores fluxos de trabalho.
* **Luigi**: O objetivo do Luigi é abordar todo o encanamento normalmente associado a processos em lote de longa duração. Se você quiser encadear muitas tarefas, automatize-as e as falhas acontecerão. Essas tarefas podem ser qualquer coisa, mas normalmente são coisas de longa duração, como tarefas do Hadoop, despejar dados de/para bancos de dados, executar algoritmos de aprendizado de máquina ou qualquer outra coisa.
* **Bonobo**: Bonobo é uma estrutura leve Extract-Transform-Load (ETL) para Python 3.5+. Ele fornece ferramentas para construir pipelines de transformação de dados, usando primitivas python simples e executando-as em paralelo. Bonobo é o canivete suíço para dados diários.
* **bubbles**: Bubbles é uma estrutura Python para processamento de dados e medição de qualidade de dados. Os conceitos básicos são objetos de dados abstratos, operações e despacho dinâmico de operações. 
* **Petl**: petl é um pacote Python de uso geral para extrair, transformar e carregar tabelas de dados.
* **pandas**: pandas é uma ferramenta de análise e manipulação de dados de código aberto rápida, poderosa, flexível e fácil de usar,
construído sobre a linguagem de programação Python.

### Para saber mais
* [Apache Airflow](http://airflow.apache.org/)
* [Luigi](https://luigi.readthedocs.io/en/stable)
* [Bonobo](https://www.bonobo-project.org/)
* [Bubbles](http://bubbles.databrewery.org/)
* [Petl](https://petl.readthedocs.io/en/stable/)
* [Pandas](https://pandas.pydata.org/)

**Referências**
* ALIEL-SAPPAGH, Shaker H.; AHMEDHENDAWI, Abdeltawab M.; BASTAWISSY, Ali HamedEl. A proposed model for data warehouse ETL processes. Journal of King Saud University - Computer and Information Sciences, [s. l.], ano 2011, v. 23, ed. 2, p. 91-104, Julho 2011.
* WILLIAM, Lourdes. Why You Need ETL Testing and What You Need to Know. [S. l.], 8 mar. 2021. Disponível em: https://www.cigniti.com/blog/why-need-etl-testing-what-need-now/. Acesso em: 16 maio 2021.

## Preparação do Projeto ETL

### Objetivos

1. Preparação do ambiente
2. Definição do projeto

## Desenvolvimento do Projeto ETL - Extração e Validação

### Objetivos da aula

1. Desenvolvimento prático do projeto de ETL
* Estração
* Validação
* Limpeza 
* Transformação
* Considerações finais (carregamento)

### Como a extração dos dados será realizada

### Realizando extração de dados parte - 1

### Realizando extração de dados parte - 2

### Como validar a extração de dados parte - 1

### Como validar a extração de dados parte - 2

### Como validar a extração de dados parte - 3

### Como validar a extração de dados parte - 4

### Como validar a extração de dados parte - 5

### Como validar a extração de dados parte - 6

## Desenvolvimento do Projeto ETL - Limpeza

### Introdução ao tema de limpeza

### Como a limpeza de dados será realizada

### Realizando a limpeza de dados - parte 1

### Realizando a limpeza de dados - parte 2

### Realizando a limpeza de dados - parte 3

### Realizando a limpeza de dados - parte 4

## Desenvolvimento do Projeto ETL - Transformação

### Introdução ao tema de Transformação

### Realizando a transformaçaõ de dados - parte 1

### Realizando a transformaçaõ de dados - parte 2

### Realizando a transformaçaõ de dados - parte 3

### Realizando a transformaçaõ de dados - parte 4

### Realizando a transformaçaõ de dados - parte 5

### Realizando a transformaçaõ de dados - parte 6

### Realizando a transformaçaõ de dados - parte 7

### Realizando a transformaçaõ de dados - parte 8

### Realizando a transformaçaõ de dados - parte 9

### Realizando a transformaçaõ de dados - parte 10

### Realizando a transformaçaõ de dados - parte 11

### Realizando a transformaçaõ de dados - parte 12

### Realizando a transformaçaõ de dados - parte 13

### Considerações finais.




