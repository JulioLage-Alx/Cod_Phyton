def minha_funcao(valor1,valor2):
    return valor1 + valor2

while True :
    valor1 = int(input("volar1: "))
    valor2 = int(input("valor2: "))

    resposta = minha_funcao(valor1, valor2)

    print(valor1,"+",valor2,"=",resposta)