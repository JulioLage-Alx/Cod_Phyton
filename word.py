salario = str(input("Digite O Valor Do Seu Salario"))

if salario <= 3000:
    print(type("Iniciante"))
elif salario > 3000 and salario <= 6000:
    print(type("pleno"))
elif salario > 6000 and salario <= 10000:
    print(type("senior"))
else : 
    print(type("Diretor"))