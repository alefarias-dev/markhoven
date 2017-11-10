# Algoritmo baseado no capitulo 8 do livro:
# Web Scraping with Python: Collecting Data from the Modern Web
# De Ryan Mitchell
# disponivel em <https://www.amazon.com.br/Web-Scraping-Python-Ryan-Mitchell/dp/8575224476/ref=sr_1_2?ie=UTF8&qid=1510320453&sr=8-2&keywords=web+scraping+with+python>
import unicodedata
import re
import random

from random import randint
from urllib.request import urlopen

# funcao para remocao de acentos
def normaliza_string(texto):
    texto = unicodedata.normalize('NFKD', texto)
    return u"".join([c for c in texto if not unicodedata.combining(c)])

# retorna o somatorio do subdicionario de uma palavra
def somatorio_lista(lista_palavras):
 soma = 0
 for palavra, valor in lista_palavras.items(): soma += valor
 return soma

# retorna uma palavra aleatoria do subdicionaro de outra palavra
# palavras que aparecem mais vezes apos a palavra 'pai' possuem
# maior probabilidade de serem escolhidas
def palavra_aleatoria(lista_palavras):
 indice_aleatorio = randint(1, somatorio_lista(lista_palavras))
 for palavra, valor in lista_palavras.items():
     indice_aleatorio -= valor
     if indice_aleatorio <= 0:
         return palavra

# constroi o dicionario baseado no input
def construir_dicionario(texto):
 # remove quebras de linha e acentos
 texto = normaliza_string(texto)

 texto = texto.replace("\\r\\n", "\n");
 texto = texto.replace("\n", " ");
 texto = texto.replace("\"", "");
 re.sub(" +"," ", texto)

 # trata pontuacao como palavras para que sejam
 # inseridas nas cadeias
 pontuacao = [',','.',';',':','!','?']
 for simbolo in pontuacao:
     texto = texto.replace(simbolo, " "+simbolo+" ");
 # lista de palavras
 palavras = texto.split(" ")
 # apenas palavras nao vazias
 palavras = [palavra for palavra in palavras if palavra != ""]
 # criacao do dicionario, literalmente
 dicionario = {}
 for i in range(1, len(palavras)):
     if palavras[i-1] not in dicionario: # se a palavra nao esta no dicionario
         # cria um novo dicionaro para esta palavra
         # o novo dicionario servirah para pegar as strings com maior
         # probabilidade de sucederem a string atual
         dicionario[palavras[i-1]] = {}
     if palavras[i] not in dicionario[palavras[i-1]]:
         dicionario[palavras[i-1]][palavras[i]] = 0
     dicionario[palavras[i-1]][palavras[i]] = dicionario[palavras[i-1]][palavras[i]] + 1
 return dicionario

# obtem input
texto = str(urlopen("file:///C:/Users/Administrador/Desktop/python/markov/training_text.txt").read())
# cria dicionario com base no input
dicionario = construir_dicionario(texto)

# gera a cadeia com o tamanho predefinido
tamanho_cadeia = 100 # define tamanho das cadeias geradas
cadeia_de_palavras = "" # inicializa nossa cadeia

# define a palavra inicial da cadeia aleatoriamente
palavra_atual = random.choice(list(dicionario))

controle_linha = 0 # apenas para controle do tamanho das linhas
for i in range(0, tamanho_cadeia):
    cadeia_de_palavras += palavra_atual+" "
    palavra_atual = palavra_aleatoria(dicionario[palavra_atual])
    controle_linha += 1
    if controle_linha == 10:
        cadeia_de_palavras += "\n"
        controle_linha = 0
print(cadeia_de_palavras)
