# Understanding and Visualizing Data with Python🐍 📊
**Curso 1 de 3**
### Week1: Introduction to Data
**Objetivos de aprendizagem**
- Desenvolver uma perspectiva para o curso e resumir conceitos e objetivos futuros
- Explore vários usos de estatísticas e examine de onde os dados se originam
- Identifique adequadamente vários tipos de dados e entenda os diferentes usos de cada um
- Entenda as funções básicas do Python para importar, limpar e gerenciar dados

#### O que é estatística
Estatística é o assunto que engloba todos os aspectos da aprendizagem a apartir dos dados e pode ser visto, como **metodologia**, se trata dos softwares ou ferramentas de trabalho, os métodos permitem o trabalho com dados para entende-los. Já os **estatísticos** aplicam e desenvolvem os métodos para enteder esses dados.
A diferença entre **estatística** e o **campo da estatística** se da no sentido de que a **estatística** nos cerca todos os dias através de previsões do tempo, ou de uma pesquisa eleitoral até mesmo a média em uma disciplina de um curso, o tempo médio que levamos para percorrer um determinado trajeto, enfim a estatística está presente no nosso dia-a-dia. O **campo de estatística** é a disciplina acadêmica focada na metodologia de pesquisa. E com relação as escolas de pensamento sobre o campo estatístico existem diferentes perspectivas sobre o campo da estatística.
- **arte de resumir dados**: Os dados podem ser enganosos, e então há a necessidade de dar sentido a esses dados, que geralmente envolve redução e sumarização. Um dos principais objetivos da reduçaõ de dados é tomar um conjunto de dados compreensível para o observador humano. Os estatísticos têm uma variedade de técnicas diferentes para resumir dados.
- Os **dados podem ser enganosos**: Uma motivação primária para desenvolver o campo das estatísticas era obter uma estrutura, uma estrutura para poder avaliar se as reivindicações baseadas em dados são significativas. Em geral, os insights dos dados não são 100% precisos, mas é certamente maravilhoso que tenhamos uma maneira de quantificar quão longe as descobertas relatadas podem estar da verdade. exe: Muitas pesquisas de opinião pública relatam resultados junto com uma margem de erro. Esta margem de erro fornece uma ideia do que será essa discrepância potencial entre os estados relatados e os estados reais da opinião pública.

**História da estatística e alguns marcos**

- Quando estamos coletando dados para sempre, nos tempos antigos, civilizações antigas têm coletado dados sobre colheitas, sobre inundações, tamanho populacional. 
- Em 1700, estamos falando sobre o desenvolvimento da teoria da probabilidade. Então, agora aleatoriedade e variação podem ser mais matematicamente definidas. 
- A estatística moderna emerge no século XIX, vindo principalmente de abordar questões que veio das áreas de genética, econometria. 
- A teoria estatística avança no século 20 com muito novas áreas de aplicação na ciência e na indústria, e, claro, o surgimento da capacidade de ter computadores para fazer essa análise de dados. 
- Então estamos nessa era de Big Data, dados massivos, ciência de dados e aprendizado de máquina.

**campos aliados da Estatística**

**Ciência da computação** para fornecer os algoritmos, as estruturas para trabalhar com dados e as linguagens de programação para manipular esses dados.
Em **Matemática** obtemos a linguagem e a notação para expressando alguns desses conceitos estatísticos de forma mais concisa, e as ferramentas capaz de avaliar e entender as propriedades desses métodos estatísticos. A **Teoria da Probabilidade** é um ramo da matemática que é parte crucial da fundação da estatística que nos permite expressar as ideias de aleatoriedade e incerteza.
Por fim a **Ciência de Dados** permite o aprendizado de máquina, gerenciamento de banco de dados ou seja provê toda infraestrutura necessária para a análise de dados.

#### O que é dado

**De onde os Dados vêm?**
Para se iniciar uma análise de dados é importante saber de onde os dados vêm e há algumas perguntas importantes que precisamos pensar sobre qual processo gerou os dados. Temos que ter em mente que existem diferentes tipos de dados com relação a origem. Mas em geral existem dois principais: um é **dados orgânicos ou de processos** são gerados por um sistema informatizado de informação extraídos de gravações de aúdios ou vídeos, são chamados de orgânicos por quê são gerados organicamente como resultado de algum processos e eles são muitas vezes gerados ao longo do tempo. exe:
- Bolsas de mercados de ações
- Histórico de visualizações da Netflix
- O hitórico do navegador na Web
- Satélites de sensoriamento remoto
- eventos esportivos

Todos esse processos geram grande quantidades de dados ou seja **Big Data** se refere a esses tipos de conjunto de dados que estão chegando de processos orgânicos, tendências ao longo do tempo onde temos muitas transações ou eventos que estamos interessados em analisar. Para o processamento de **big data** é necessário recursos computacionais significativos. Então o que os cientistas de dados fazem é **estrair esses dados para estudar tendências e descobrir relacionamentos interessantes**.
Outro tipo de dados que podemos estar trabalhando são os chamados **dados projetados ou coletados**, diferente dos dados orgânicos esses tipos de dados são decorrentes de uma coleta de dados de design ou seja são estudos bem específicos que são projetados especificamente para abordar um objetivos específico de investigação.

#### Usando Python para ler arquivos e explorar seus conteúdos

