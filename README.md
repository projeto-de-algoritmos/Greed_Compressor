# Greed Compressor

**Conteúdo da Disciplina**: Algoritmos Ambiciosos (Greed)<br>
**Tema**: Compressão de dados

## Alunos
|Matrícula | Aluno | GitHub |
| -- | -- | -- |
| 15/0009011  |  Elias Bernardo | @ebmm01
| 17/0141161  |  Erick Giffoni | @ErickGiffoni

## Sobre 

**Greed Compressor** é um compressor de dados que funciona via execução pelo terminal/shell. <br>
Com ele você consegue comprimir um arquivo de texto no formato .txt  e gerar um arquivo binário com  <br> tamanho reduzido, bem como descomprimir um arquivo em binário (no formato .greed_compressed) <br>para voltar ao original.<br>

**Greed Compressor** funciona segundo o [algoritmo de compressão de dados de Huffman](https://en.wikipedia.org/wiki/Huffman_coding)


**Linguagem**: Python 3.8<br>
**Biblioteca(s)**: [bitstring](https://pypi.org/project/bitstring/), [pyfiglet](https://pypi.org/project/pyfiglet/0.7.5/)

### Requisitos para utilizar esse projeto

- conexão de internet;<br>
- terminal/console/shell no computador;<br>
- pip & venv
- **Python 3.8** (necessariamente)
- clonar o projeto;

> Para clonar o projeto digite:

    git clone https://github.com/projeto-de-algoritmos/Greed_Compressor.git

## Screenshots

### Versão Terminal - v1.0

- Menu inicial

![](images/terminal_home.png)

<hr>

- Compressão de arquivo realizada

![](images/terminal_compressed.png)

<hr>

- Descompressão de arquivo realizada

![](images/terminal_descrompressed.png)

## Instalação 

Após fazer o clone do projeto, siga os passos abaixo :

- entre na raiz do projeto

>
    $ cd Greed_Compressor/

- (Opcional) Caso não possua uma venv, gere uma:

>
    $ python -m venv <nome da venv>

- (Opcional) Ative a venv caso não esteja:

> Note que o comando abaixo pode variar de acordo com o sistema operacional. Em caso de dúvidas veja a [documentação](https://docs.python.org/pt-br/dev/library/venv.html)
>
    $ source venv/bin/activate

- instale as dependências

>
    $ python -m pip install -r requirements.txt

- execute o projeto

> Para a versão terminal:
>
    $ python -m view.terminal.main

## Uso 

### Terminal - v1.0

TODO - Vídeo de apresentação

- É necessário ter o Python 3.8

Com o projeto em execução escolha uma das opções numéricas do menu principal:

````
1 - Codificar arquivo
2 - Decodificar arquivo
0 - Sair/ Terminar execução
````
Feito isso, siga as instruções em tela.

## Problemas ? Sugestões ?

Caso você tenha alguma dificuldade, sugestão ou algum problema com o projeto,<br>
por favor entre em contato conosco:

- Elias Bernardo - ebmm01@gmail.com - telegram @ebmm01
- Erick Giffoni - giffoni.erick@gmail.com - telegram @ErickGiffoni<br>





