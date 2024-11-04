from password_service import *
from file_service import *

usuario_escolha = input("quantos digitos na senha? ")
    #checamos se o usuario nao vai ter 2 neuronios e inputar algo que nao seja um numero
if usuario_escolha.isdigit():
        usuario_escolha = int(usuario_escolha)
else:
    print("ENTRADA INVALIDA!")
    quit()

#agora chamamos a função se nao ela nao vai ser usado

resposta = gerador_senha(Len_senha = usuario_escolha)
print(f"senha gerada:\n{resposta}")
export_output(resposta)