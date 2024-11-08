#Pulls de biblioteca e def
from datetime import datetime
import os
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



def export_output(output):
    # Define o diretório onde os arquivos serão salvos
    directory = "Senhas_geradas"
    
    # Cria o diretório se ele não existir
    os.makedirs(directory, exist_ok=True)
    
    # Gera um nome de arquivo com timestamp para evitar sobrescrita
    filename = os.path.join(directory, f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # Salva o conteúdo do output no arquivo
    #o "with, as" garante que o arquivo vai ser aberto e fechado
    #open vai abrir o arquivo como escrita e depois o output vai ser salvo como string (pra facilitar)
    with open(filename, "w") as file:
        file.write(str(output))
    
    print(f"Output salvo em: {filename}")

usuario_escolha = input("quantos digitos na senha? ")
    #checamos se o usuario nao vai ter 2 neuronios e inputar algo que nao seja um numero
if usuario_escolha.isdigit():
        usuario_escolha = int(usuario_escolha)
else:
    print("ENTRADA INVALIDA!")
    quit()

#agora chamamos a função se nao ela nao vai ser usada

resposta = gerador_senha(Len_senha = usuario_escolha)
print(f"senha gerada:\n{resposta}")
export_output(resposta)

