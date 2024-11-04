import random
import string
from file_service import *


def gerador_senha(Len_senha = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options
    # a soma irá concatenar as opções

    senha_do_usuario = ""
    for i in range(0, Len_senha):
        # i é uma variavel auxiliar
        # cria um array de 0 ao lensenha começando do indice 0
        # a string no python TAMBEM é uma lista
        digit = random.choice(options)
        senha_do_usuario = senha_do_usuario + digit
    
    return senha_do_usuario
    #nada depois do return vai ser executado