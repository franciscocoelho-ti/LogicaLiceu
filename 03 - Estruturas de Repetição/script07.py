# Dado um número inteiro positivo, determine a sua decomposição em fatores primos. A saída do programa deve ser semelhante ao exemplo abaixo:

# 180 | 2
#  90 | 2
#  45 | 3
#  15 | 3
#   5 | 5
#   1


numero = int(input('Informe um número a ser decomposto: '))
fator = 2

while numero > 1:
    if numero % fator == 0:
        print(f'{numero:3.0f} | {fator}')
        numero = numero / fator
    else:
        fator = fator + 1

print(f'{numero:3.0f}')
