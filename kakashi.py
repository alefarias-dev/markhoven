import re
from unidecode import unidecode

import requests as req
from urllib.error import HTTPError
from bs4 import BeautifulSoup


MUSIC_SOURCE = "https://www.letras.mus.br";
AUTORES = ["chico-buarque"]


def normaliza_string(texto):
    texto = unidecode(texto)
    texto = texto.lower()
    return texto


def obtem_pagina_autor(url_autor):
    url_autor = f"{MUSIC_SOURCE}/{autor}"
    resposta = req.get(url_autor)
    if checa_resposta(resposta):
        return BeautifulSoup(resposta.text, "html.parser")
    return None


def obtem_pagina_musica(url_musica):
    url_musica = f"{MUSIC_SOURCE}{url_musica}"
    resposta = req.get(url_musica)
    if checa_resposta(resposta):
        return BeautifulSoup(resposta.text, "html.parser")
    return None


def checa_resposta(resposta_requests):
    if resposta_requests.status_code != 200:
        return False
    return True


def obtem_titulo_musica(pagina_musica):
    try:
        titulo_musica = pagina_musica.find("div",{"class":"cnt-head_title"})
        titulo_musica = titulo_musica.find("h1").get_text()
    except AttributeError as e:
        titulo_musica = "NA"
    return titulo_musica


def obtem_letra_musica(pagina_musica):
    tags_musica = pagina_musica.find("div", {"class": "cnt-letra"})
    if tags_musica:
        return tags_musica.text
    return None


temporario = ""
for autor in AUTORES:
    print(f"\nMinerando musicas de: {autor}")

    pagina_autor = obtem_pagina_autor(autor)
    lista_musicas = pagina_autor.find("ol", {"class":"cnt-list"}).findAll("li")

    for musica in lista_musicas:
        a_musica = musica.find("a")

        if "href" in a_musica.attrs:
            link = a_musica.attrs['href'] # obtem o link para musica
            
            print(f"{MUSIC_SOURCE}{link}")
            pagina_musica = obtem_pagina_musica(link)
            titulo_musica = obtem_titulo_musica(pagina_musica)
            letra_musica = obtem_letra_musica(pagina_musica)
            temporario += normaliza_string(letra_musica)+"\n"
            print(f"Musica: {titulo_musica} copiada.")


# escreve no arquivo
with open("training_text.txt", "w") as arquivo:
    arquivo.write(temporario)
