import os
mensagem =[]

nome = input("Nome:")

while True:
    os.system('cls')

# LIMPANDO O TERMINAL
    if len(mensagem) > 0:
        for m in mensagem:
            print(m["nome"],"-",m['texto'])

    print("______________")

#OBTENDO TEXTO 
    texto = input("mesnsagem")
    if texto == "fim":
        break

#ADICIONANDO MENSAGEM NA LISTA 
    mensagem.append({
        "nome":nome,
        "texto": texto


    })