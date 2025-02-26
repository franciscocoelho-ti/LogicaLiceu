# Escreva um algoritmo em Python que leia uma sequência de números inteiros terminadas por -1 e imprima na tela o maior e o menor número lido.
# Obs.: O valor -1 é somente um terminador e não deve ser considerado nos cálculos.

numero = None
contador = 1
menor_numero = None
maior_numero = None

while numero != -1:
    numero = int(input('Informe um número: '))

    if contador == 1:
        menor_numero = numero
        maior_numero = numero
        # Incrementar o contador para não entrar mais no IF
        contador += 1
    else:
        if numero < menor_numero and numero != -1:
            menor_numero = numero
        elif numero > maior_numero:
            maior_numero = numero

print(f'O menor número informado foi: {menor_numero}')
print(f'O maior número informado foi: {maior_numero}')



    

