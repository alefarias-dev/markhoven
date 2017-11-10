# kakashi eh um crawler ninja copiador de letras de musicas
# de algum autor qualquer selecionado adicionando ao arquivo
# training_text.txt
import re
import unicodedata

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def normaliza_string(texto):
    texto = unicodedata.normalize('NFKD', texto)
    return u"".join([c for c in texto if not unicodedata.combining(c)])

# buscaremos letras cadastradas no site letras
music_source = "https://www.letras.mus.br";
# esses sao nossos autores de interesse
autores = ['/chico-buarque']

# string que mantera as musicas
temporario = ""
modo = "w"
sobrescreve = input("Sobrescrever arquivo de treino? (S/N)")

for autor in autores:
    print ("\nMinerando musicas de: "+autor)
    # abre a pagina do artista e transforma em um
    # objeto BeautifulSoup
    html = urlopen(music_source+autor)
    bs = BeautifulSoup(html, "html.parser")

    # pega a lista de todas as musicas
    lista_musicas = bs.find("ul", {"class":"cnt-list"})
    lista_musicas = lista_musicas.findAll("li")

    # pra cada musica
    counter = 20
    for musica in lista_musicas:
        counter -= 1
        a_musica = musica.find("a")
        if "href" in a_musica.attrs:
            link = a_musica.attrs['href'] # obtem o link para musica
            try:
                pagina_musica = urlopen(music_source+link).read()
                pagina_musica = BeautifulSoup(pagina_musica, "html.parser")

                try:
                    titulo_musica = pagina_musica.find("div",{"class":"cnt-head_title"})
                    titulo_musica = titulo_musica.find("h1").get_text()
                except AttributeError as e:
                    titulo_musica = "NA"

                letra_musica = pagina_musica.find("article")
                letra_musica = str(letra_musica).replace('<p>', '')
                letra_musica = letra_musica.replace('</p>', '\n')
                letra_musica = letra_musica.replace('<article>', '')
                letra_musica = letra_musica.replace('</article>', '')
                letra_musica = letra_musica.replace('<br/>', '\n')
                letra_musica = letra_musica.replace('\'', '')

                temporario += normaliza_string(str(letra_musica))+"\n"
                print("Musica: "+titulo_musica+" copiada pelo sharingan sinfonico.")

            except HTTPError as e:
                print(music_source+link+" falhou")
            if counter == 0: break

# escreve no arquivo
if sobrescreve.lower() == "n": modo = "a"
arquivo = open("training_text.txt", modo)
arquivo.write(temporario)
arquivo.close()
