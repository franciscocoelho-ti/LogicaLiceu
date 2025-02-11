# Escreva um algoritmo em Python que leia dois números inteiros, correspondentes ao dividendo e ao divisor de uma divisão, e mostra o quociente. O algoritmo deve impedir que se efetue uma divisão por zero e imprimir uma mensagem de erro quando isso ocorrer.

try:
    # Entrada: Receber os dados do usuário
    dividendo = int(input('Informe o dividendo: '))
    divisor = int(input('Informe o divisor: '))

    # Processamento
    quociente = dividendo / divisor

    # Saída
    print('O resultado foi: ', quociente)

except ZeroDivisionError:
    print('Erro: Impossível dividir por zero.')

except ValueError:
    print('Erro: Informe sempre números')


