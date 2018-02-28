## Computação científica para biólogos

### Sumário

[**Introdução: o porquê deste curso**](./Introdução.html/)

I.1 Apresentação  
I.2 Informática cada vez mais necessária  
I.3 As ferramentas

[**Módulo 1: Ferramentas básicas**](./Módulo\ 1.html)

1.1 - Linha de comando: Terminal  
1.2 - Editor de texto e IDE: Atom	
1.3 - Linguagem de Programação: Python

[**Módulo 2: Bibliotecas e ambientes virtuais**](./Módulo 2.html)

2.1 - Conda: Ambientes virtuais e instalação de dependências  
2.2 - Bibliotecas essenciais: Jupyter, Pandas e Matplotlib.  
2.3 - Analisando o conjunto Iris no Jupyter Notebook  

[**Módulo 3: Colaboração e boas práticas**](./Módulo 3.html)

3.1 - Boas práticas em computação científica  
3.2 - Documentação e controle de versão: Git e GitHub  
3.3 - Como aprender programação: dicas para biólogos

-

## Módulo 3:

<!---
To-do:

- importância da colaboração
- ten simple rules for biologists learning to program
- boas praticas:
	- documentação com jupyter notebook
	- controle de versão com git
	- colaboração com github


-->

### 3.1 - Boas práticas em computação científica

**Referências:**
 
   
[[1]](./papers/Wilson et al 2017 Good enough practices scientific computing.pdf) **Wilson et al, 2017.** Good enough practices in scientific computing


<!-- TRANSFERIR ESSA SEÇÃO PARA INTRODUÇÃO

Recapitulando o que foi discutido na [Introdução](./introdução.md) do curso, a proficiência no uso do computador e o domínio de fundamentos básicos de programação estão se tornando cada vez mais indispensáveis para qualquer cientista. Apesar das necessidades relacionadas ao treinamento dos pesquisadores neste tópico já serem evidentes há certo tempo, só em anos recentes que essa discussão se tornou bem presente na literatura. Comentários na revista Nature [[1]](./papers/Loman & Watson 2013 So you want to be a computational biologist.pdf) e essa carta [[2]](./papers/Welch 2014 Bioinformatics curriculum.pdf) da ISCB (International Society for Computational Biology) descrevem habilidades-chave para biólogos que querem tirar proveito das ferramentas computacionais. Cientistas blogueiros também já escreveram sobre isso em meios menos formais do periódicos acadêmicos. Em 2009, o geneticista [Daniel MacArthur](https://www.wired.com/author/daniel-macarthur/) escreveu para revista Wired [[3]](./papers/MacArthur 2009 Why biology students should learn how to program _ WIRED.html), falando sobre informática:  **"não consigo pensar em quase nenhuma outra área na qual investir tempo e esforço cedo em sua carreira pode trazer um retorno tão dramático em termos de produtividade científica e oportunidades de carreira."** (adaptado)

--> 
Nos Módulos 1 e 2 já fomos introduzidos à uma variedade de ferramentas que serão essenciais no nosso caminho da informática. Conseguimos fazer análise e visualização do conjunto de dados "Iris" usando comandos Python, no nosso Jupyter Notebook ou na nossa interface Atom + Terminal. Vimos diversos recursos para aprender a linguagem, como baixar e instalar bibliotecas e como organiza-las em ambientes virtuais; para integrar todos esses conhecimentos, temos que nos concentrar em adotar **boas práticas de computação científica**.

Através de suas experiências com os workshops da *Software Carpentry*, Greg Wilson e colegas [[1]](./papers/Wilson et al 2017 Good enough practices scientific computing.pdf) destacaram a carência dessas práticas e elaboraram um sumário de regras gerais que cientistas podem e devem considerar adotar. O título do paper, "Práticas boas o suficiente em computação científica" (adaptado) já faz alusão ao fato de que o exercício de tais práticas não deve ser algo cansativo e perfeccionista, mas sim princípios básicos no qual devemos nos apoiar na hora de trabalhar no computador, **da mesma forma que fazemos na bancada**. 

Isso significa que *workflows* computacionais devem seguir as mesmas práticas que outros projetos de laboratório, incluindo dados organizados, passos documentos e uma estruturação do projeto voltada à *reprodutibilidade*. Se usamos métodos computacionais para manipular nossos dados, eles devem ser descritos na literatura; A regra geral é sempre citar os softwares que foram utilizados, especialmente se há um paper descrevendo a ferramenta. No entanto, assim como um protocolo de laboratório, o processamento de dados pode variar dependendo de como a ferramenta computacional é utilizada. Imagine um ensaio enzimático: a concentração de determinado reagente pode influenciar o resultado final, certo? O mesmo acontece com ferramentas de informática: A configuração de determinados parâmetros em um software pode alterar a saída de dados, e consequentemente a informação a ser interpretada. Portanto, não basta citar apenas o método utilizado, e também **como** foi utilizado.

O paper de Wilson et al., fornece um guia detalhado, porém simples, de como essas práticas proporcionam um "controle de qualidade" no processo de pesquisa, visando facilitar a execução pelo próprio usuário e também garantindo sua reprodutibilidade para terceiros. Hoje em dia, é muito fácil se perder na montanha de dados e análises de qualquer projeto, por mais singelo que seja, logo fica a dica da leitura para qualquer pesquisador no século XXI. Suas recomendações se dividem nos seguintes tópicos:

* **Gerenciamento de dados *(data management)*:** salvar ambos dados originais ("*raw*") e intermediários, documentar todos os passos, criar dados limpos compatíveis com a análise.
* ***Software:*** escrever, organizar e compartilhar *scripts* e programas usados em uma análise.
* **Colaboração:** facilitar para que colaboradores existentes e novos como entender e contribuir para um projeto.
* **Organização de projeto:** organizar os artefatos digitais de um projeto de forma a facilitar sua descoberta e entendimento.
* **Monitoramento de mudanças:** registrar como os diversos componentes de seu projeto mudam ao longo do tempo.

(adaptação livre do artigo)

### 3.2 - Documentação e controle de versão: Git e GitHub.

Como já foi discutido, para garantir o rigor científico de uma análise, é necessário documentar todos os passos. Assim como na ciência precisamos descrever nossa metodologia, quando estamos programando precisamos documentar nosso código. O que isso significa é que devemos explicar como nosso programa funciona, o que cada linha de código faz e como utilizar funções. Fazemos isso através de **comentários.**

Nos Jupyter Notebooks deste curso já vimos comentários. São linhas de código precedidas de algum caracter (em Python, `#` ou texto entre os caracteres `'''` ou `" " "`).

Imagina se formos ter que usar aquele mesmo código daqui a 6 meses? Será que a gente vai entender o que cada coisa faz? Por isso é importante adicionar comentários à medida que um arquivo de código vai acumulando linhas. Quando escrevemos programas mais complexos, a documentação não se refere somente aos comentários, mas a um conjunto de documentos que vão auxiliar usuários e desenvolvedores daquele programa. Arquivos como "README.txt", "requirements.txt" ou "LICENSE.txt" são exemplos de documentos. Documentação é um aspecto fundamental para a prática de programação, no entanto no momento podemos nos contentar com adicionar comentários úteis em nossos humildes scripts.

Uma análise realizada através de código pode ser documentada da mesma forma que um programa que já foi desenvolvido. Por exemplo, [nessa página](https://github.com/vinisalazar/BioEnergia-Lagoa/blob/master/Lagoa%20BioEnergy%20Project%2016S%20Analysis%20Workflow.md) temos um *workflow* para análise de uma comunidade microbiana a partir de amplificação e sequenciamento do gene rRNA 16S. O arquivo é do tipo .md (MarkDown), ou seja, um arquivo de texto contendo os comandos executados no Terminal utilizando os pacotes PEAR e QIIME. Repare como as versões de cada pacote, bem como a base de dados de referência (SILVA), foi referenciada. Cada comando (ou passo do protocolo) é precedido de uma explicação e aparece exatamente como foi digitado.

Apesar de ser o suficiente para reproduzir a análise, esse documento falha em um aspecto, que é o de não *printar* o *output* de cada comando. Como já foi visto conseguimos fazer isso no Jupyter Notebook! Podemos mesclar texto em MarkDown, código com os devidos comentários e ainda podemos visualizar o output, como fizemos com o conjunto Iris!

A prática de documentação de forma distinta para cada uma dos cinco tópicos de boas práticas propostos por Greg Wilson. Nossa próxima prática importante será a de usar um programa de **controle de versão.**

![](../screens/git2.png)

Todos nós já passamos por aquela situação de ter vários arquivos parecidos com nomes do tipo "rascunho.doc", que viram "versaofinal.doc", depois "v\_final2.doc", "v\_finalcorrigida.doc", "vfinal\_agora_vai.doc"

**Git** é um programa que monitora as mudanças em nossos projetos, e permite criar *checkpoints* em nossos arquivos e diretórios. Basicamente, nosso trabalho envolve os seguintes passos:

* Criar coisas
* Salvar coisas
* Editar coisas
* Salvar a coisa de novo

No quarto passo, salvar novamente, que controle de versão irá nos auxiliar. Podemos registrar **o que foi alterado**, **quando** aconteceu a mudança, e comparar o **antes** e **depois.**

![](../screens/git.png)

Dessa forma, gerenciamos as versões do nosso projeto, como se tirassemos pequenos retratos (*snapshots*) de cada versão do projeto.

Para ter uma ideia melhor de como o Git funciona, [siga o tutorial no site (em inglês)](https://try.github.io/levels/1/challenges/1)

Apesar de vermos como funciona no site, é interessante fazer uma demonstração local na nossa máquina. Primeiro, [certifique-se que você tem o Git instalado.](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) Vamos criar um diretório, inicializar o Git nesse diretório, criar um arquivo de texto, adiciona-lo ao nosso arquivo Git, e realizar um *commit*, ou seja, registrar a mudança que realizamos no nosso projeto.

<!-- Módulo 3 - git.ipynb -->

Se fosse o caso de 