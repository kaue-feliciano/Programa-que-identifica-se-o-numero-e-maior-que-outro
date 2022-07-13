valor1 = int(input("Digite um valor"))
valor2 = int(input("Digite outro valor"))
if valor1 > valor2:
    print("o numero {} e maior que o numero {}".format(valor1,valor2))
elif valor1 == valor2:
    print("os valores {} e {} sao iguais".format(valor1 ,valor2))
else:
    print("o numero {} e maior que o numero {}".format(valor2 , valor1))