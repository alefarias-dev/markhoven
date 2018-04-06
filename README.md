Markhoven!
===================
![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/AAMarkov.jpg/220px-AAMarkov.jpg)

[TOC]


## Repositório
Bem vindo, 
o repositório contem três arquivos, kakashi.py é um ninja copiador de letras de músicas que estão hospedadas no site letras.mus.br

markovhen.py é o algoritmo responsável pela geração de cadeias de palavras utilizando o conceito das cadeias de Markov.
	
## Uma breve descrição sobre os algoritmos
### kakashi.py

O algoritmo **kakashi.py** é um crawler que utiliza a biblioteca BeautifulSoup para minerar as letras das músicas de cada artista.
	
Essencialmente, para que funcione de acordo com suas necessidades, kakashi precisa que você dê a ele os caminhos para cada artista, por conveniência, não é tão complicado obter este tipo de informação do site letras.mus.br, todas as páginas de artista seguem o padrão:
> letras.mus.br/nome-artista

da mesma forma as músicas seguem:
> letras.mus.br/nome-artista/nome-musica

Aproveitando dessa padronização, dado o endereço da página de qualquer artista, kakashi deve ser capaz de copiar todas as letras de músicas que encontrar (com certas restrições, o algoritmo define um limite máximo de até 20 músicas por artista, nada que não possa ser modificado posteriormente).

Por fim, todas as letras são salvas no arquivo **training_text.txt**

### markov.py
Já o algoritmo **markov.py** é o responsável por toda a magia envolvendo as cadeias de Markov, a ideia essencial por trás de seu funcionamento está em gerar um dicionário de palavras através do arquivo de treinamento, e com base neste texto de treino montar para cada palavra subdicionarios contendo a frequência das palavras que as sucedem.

Dessa forma, dado qualquer palavra do dicionário, uma função seleciona aleatoriamente uma palavra que (em geral) possui alto potencial de ser uma sucessora daquela que estávamos olhando.

## Primeiros testes 

Em geral os algoritmos ainda precisam de otimizações, mesmo assim podemos obter alguns resultados interessantes.

Começamos por minerar músicas de Chico Buarqe:
```
Sobrescrever arquivo de treino? (S/N)s
Minerando musicas de: /chico-buarque
Musica: A Aurora de Nova York copiada pelo sharingan sinfonico.
Musica: A Banda copiada pelo sharingan sinfonico.
Musica: A Bela e a Fera copiada pelo sharingan sinfonico.
Musica: A Cidade Dos Artistas copiada pelo sharingan sinfonico.
Musica: A Cidade Ideal copiada pelo sharingan sinfonico.
Musica: A Foto da Capa copiada pelo sharingan sinfonico.
Musica: A Galinha copiada pelo sharingan sinfonico.
Musica: A História de Lily Braun copiada pelo sharingan sinfonico.
Musica: A Ilha copiada pelo sharingan sinfonico.
Musica: A Mais Bonita copiada pelo sharingan sinfonico.
Musica: A Mão da Limpeza copiada pelo sharingan sinfonico.
Musica: A Moça do Sonho copiada pelo sharingan sinfonico.
Musica: A Mulher de Cada Porto copiada pelo sharingan sinfonico.
Musica: A Mulher do Aníbal (part. Zeca Pagodinho) copiada pelo sharingan sinfonico.
Musica: A Noiva da Cidade copiada pelo sharingan sinfonico.
Musica: A Ostra e o Vento copiada pelo sharingan sinfonico.
Musica: A Permuta Dos Santos copiada pelo sharingan sinfonico.
Musica: A Pousada do Bom Barão copiada pelo sharingan sinfonico.
Musica: A Rita copiada pelo sharingan sinfonico.
Musica: A Rosa copiada pelo sharingan sinfonico.
```

Finalmente executamos **markov.py**, as cadeias tem tamanho predefinido de 100 palavras/simbolos, e seu tamanho pode ser parametrizado facilmente:
```
homem serio que e Imagina so O Ze do teatro 
Dados juntos E um duo . Voce tambem vem ? 
Cachorro : Sim , afinal , olha , o mar 
Se o branco sujava , voce Porque nao e aquela 
pensao Se eu sou teu condao Oh bela tramoia Ja 
vou com os varredores E uma gema Me apareceu no 
meio da banda passar Cantando coisas Tao puras Que bode 
, mas isso e Imagina so pruma noite escura Mas 
escuta o chapeu Ser artista Na verdade a entrada Vai 
ouvir e . Vou procurar emprego como star Me apareceu 
```






