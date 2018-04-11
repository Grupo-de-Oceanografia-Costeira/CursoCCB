## Computação científica para biólogos e pesquisadores

### Sumário

[**Introdução: o porquê deste curso**](./introducao.md/)

I.1 Apresentação  
I.2 Informática cada vez mais necessária  
I.3 As ferramentas

[**Módulo 1: Ferramentas básicas**](./modulo_1.md)

1.1 - Linha de comando: Terminal  
1.2 - Editor de texto e IDE: Atom  
1.3 - Linguagem de Programação: Python

[**Módulo 2: Bibliotecas e ambientes virtuais**](./modulo_2.md)

2.1 - Conda: Ambientes virtuais e instalação de dependências  
2.2 - Bibliotecas essenciais: Pandas, Matplotlib e Jupyter  
2.3 - Analisando o conjunto Iris no Jupyter Notebook  

[**Módulo 3: Colaboração e boas práticas**](./modulo_3.md)

3.1 - Boas práticas em computação científica  
3.2 - Documentação e controle de versão: Git e GitHub  
3.3 - Como aprender programação: dicas para biólogos

-
## Módulo 2:

### 2.1 Conda: ambientes virtuais e dependências

### Pacotes e bibliotecas

Assim como o `R`, a capacidade do `Python` é enormemente expandida por conta da grande quantidade de pacotes e bibliotecas disponíveis. Alguns são essenciais para quem quer realizar análise de dados.

![Existem muitas bibliotecas de Python voltadas à análise de dados biológicos](../img/biopython.png).

[Nesse tópico no site BioStars](https://www.biostars.org/p/50749/#50758), esse usuário apontou algumas ferramentas em Python que são úteis para biólogos.

Logo, é imprescindível aprender a baixar, instalar e rodar esses pacotes. Essa instalação é simples, mas é diferente de usar um "Install Wizard": geralmente é feita pela linha de comando.

![Install wizard do RStudio](../img/rstudio.jpg)

Você pode até se safar instalando o RStudio usando um Install Wizard, mas para instalação de pacotes Python vai ter que recorrer ao Terminal.

Além disso, existe outra questão: muitos pacotes dependem de outros para funcionar, e todos dependem de ter uma instância de Python instalada. Pior, às vezes pacotes requerem versões **específicas** de outro pacote ou linguagem, e pacotes que requerem versões **diferentes** podem causar o que chamamos de um **conflito de dependência**.

### Ambientes virtuais: caixinhas no computador

Para instalarmos uma biblioteca, precisamos de um programa que faça isso para nós, um **gerenciador de pacotes**. Por sorte, o Python vem com um instalado de fábrica, o [`pip`](https://pip.pypa.io/en/stable/): pip installs packages. O `pip` faz download e instala pacotes disponíveis no [PyPI - Python Package Index](https://pypi.python.org/pypi), um repositório de bibliotecas aberto mantido pela Python Software Foundation. O `pip` funciona muito bem, no entanto queremos mais que isso.

Para isso instalamos o Anaconda, que é uma plataforma para ciência de dados que inclue um gerenciador de pacotes chamado [`conda`](https://conda.io/docs/index.html). Além de baixar e instalar pacotes, o `conda` também gerencia **ambientes virtuais**.

**Mas o que são e por que precisamos de ambientes virtuais?**

Ambientes virtuais (*virtual environments* ou *envs*), são como caixinhas em nosso computador na qual instalamos programas, pacotes, bibliotecas, ou dependências, e elas funcionam naquele ambiente fechado, sem interferir com outras instalações fora desse ambiente.

**Por exemplo:**

Quando vamos baixar o Anaconda, podemos escolher entre Python versão 2.7 ou 3.4. Digamos que escolhemos a 3.4, por que é mais atualizada e compatível com a maioria dos programas. Porém, estamos fazendo um estudo de microbiologia e para analisar nossos dados, vamos precisar do [QIIME](http://qiime.org/), que requere a versão 2.7 do Python para rodar, e é incompatível com as versões 3.x. Além do Python, o QIIME requere versões específicas de diversas outras bibliotecas, que podem interferir com nosso ambiente **root** (nosso ambiente "global", sem nenhum ambiente virtual ativado. Sim, o nosso sistema operacional usa uma versão de Python para executar várias outras atividades, que nada tem a ver com o Conda).

A solução é **criar um ambiente virtual** com Python 2.7 instalado, e nesse ambiente instalamos as **dependências** necessárias para que o QIIME rode. O `conda` permite que façamos isso.

[![Quantitative Insights Into Microbial Ecology](../img/qiime.png)](http://qiime.org/)

### Criando um ambiente virtual

Embora a instalação do Anaconda nos propicia o Anaconda Navigator, uma interface gráfica, vamos utilizar o `conda` pelo Terminal.

[Nesse documento](papers/conda-cheatsheet.pdf) temos uma referência rápida dos comandos básicos do `conda`.

Para criar um novo ambiente, usamos o comando `conda create` junto do nome do ambiente e a versão de Python que desejamos.

`conda create --name qiime python=2.7`

Agora que temos um ambiente com a versão que precisamos, podemos instalar o QIIME e o restante de suas dependências.

Ativamos o novo ambiente com o comando:
`source activate qiime`

### Instalando pacotes do Anaconda Cloud

Diferente do `pip`, o `conda` não baixa programas do [PyPI](https://pypi.python.org/pypi), e sim de outra base de dados, a [Anaconda Cloud.](https://anaconda.org/)

[![https://anaconda.org/](../img/anaconda.png)](https://anaconda.org/)

Esse repositório é muito útil pois fornece os pacotes disponíveis e os comandos para instalação.

[![https://anaconda.org/bioconda/qiime]((../img/qiimeinstall.png)](https://anaconda.org/bioconda/qiime)

Copiamos o comando e uma mensagem irá confirmar a instalação do QIIME e todas as dependências necessárias.

`conda install -c bioconda qiime`

Acontece que perdemos todas as nossas sequências, então não vamos precisar do QIIME. Vamos aprender sobre outras bibliotecas mais essenciais no momento. Então, para remover ese ambiente virtual criado use os comandos:
`source deactivate`
`conda remove -n qiime --all`

Vamos criar um novo ambiente virtual para fazer uma análise de dados mais simples. Além da versão do Python, podemos especificar outros pacotes para o `conda` instalar quando criar o ambiente:

`conda create -n tutorial Python=3 Pandas Matplotlib Jupyter`

Selecionamos Python 3, bem como as bibliotecas [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), [Jupyter](http://jupyter.org/) e suas dependências.

Ativando o ambiente:

`source activate tutorial`

É importante aprender os diferentes comandos do `conda`. Outros gerenciadores de pacote como o `pip` também funcionam com comandos como `pip install <nome do pacote>`. Você pode utilizar o `pip` para instalar pacotes em ambientes criados pelo `conda`. Para ver os pacotes que estão no ambiente atual, use o comando `conda list`. Um sumários dos comandos do `conda` pode ser acessado [nessa *cheat sheet*.](./conda-cheatsheet.pdf)


### 2.2 Bibliotecas essenciais: Pandas, Matplotlib e Jupyter.

É um equívoco comum, para quem está começando a aprender uma linguagem, pensar que o uso desta por si só vai levar ao resultado final do que se está buscando. Uma linguagem como Python, embora poderosa, necessita um conhecimento extenso para ser utilizada efetivamente sem o auxílio de pacotes externos. 

Para tirar o máximo proveito de um conhecimento básico de Python, vamos alavancar a funcionalidade da linguagem por meio dessas três bibliotecas. Sua combinação vai nos possibilitar um ambiente simples mas efetivo para análise de dados. Se o nosso objetivo fosse outro, como por exemplo, desenvolvimento web, faríamos uso de outras bibliotecas, como os *frameworks* [Flask](http://flask.pocoo.org/) ou [Django.](https://www.djangoproject.com/)

[![https://pandas.pydata.org/]((../img/pandas.png)](https://pandas.pydata.org/)

[Pandas](https://pandas.pydata.org/) é uma biblioteca de análise contendo ferramentas de análise de dados de fácil uso e alta performance. Vamos utilizar **métodos** dessa biblioteca para importar e manipular nossos dados.

[![https://matplotlib.org/]((../img/matplotlib.png)](https://matplotlib.org/)

[Matplotlib](https://matplotlib.org/) é uma biblioteca de plotagem inspirada no MATLAB, com a diferença de ser de graça e *open source*. Oferece uma variedade de ferramentas para plotar os dados que criamos com Pandas.

[![http://jupyter.org/]((../img/jupyter.png)](http://jupyter.org/)

[Jupyter](http://jupyter.org/) é uma biblioteca muito interessante que nos fornece o [Jupyter Notebook](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks), uma ferramenta muito útil para organizar um projeto de análise de dados.

Um arquivo Jupyter Notebook permite a *execução de código* junto com texto MarkDown, como html. Vamos realizar nossa análise com `Pandas`, plotar com `Matplotlib` e anotar e organizar tudo com anotações utilizando o `Jupyter Notebook`.

O arquivo [python\_primeiros_comandos.html](./python_primeiros_comandos.html) foi renderizado a partir de um arquivo Notebook. Vamos abrir o arquivo [modulo\_2_continuacao.ipynb](../notebooks/modulo\_2_continuacao.ipynb). Mas para isso precisamos abrir uma instância de Jupyter.

No Terminal, digite `Jupyter Notebook` para abrir uma página no seu navegador web.

-
