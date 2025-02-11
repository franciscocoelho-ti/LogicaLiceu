# Escreva um algoritmo em Python que leia 3 números inteiros e verifique se estes podem formar um triângulo, ou seja, a soma de dois lados tem que ser necessariamente maior que o terceiro lado.
# Caso os valores formem um triângulo, verificar se é um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes).
# Imprima uma mensagem conforme o resultado obtido.

lado1 = int(input('Informe o valor do 1º lado: '))
lado2 = int(input('Informe o valor do 2º lado: '))
lado3 = int(input('Informe o valor do 3º lado: '))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and(lado1 + lado3 > lado2):
    # Dentro do IF que determina um triângulo, vamos verificar que tipo de triângulo forma.
    if (lado1 == lado2) and (lado2 == lado3):
        print('Os valores formam um triângulo equilátero')
    elif (lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3):
        print('Os valores formam um triângulo escaleno')
    else:
        print('Os valores formam um triângulo isósceles')

else:
    print('Não forma um triângulo')

                                                            
