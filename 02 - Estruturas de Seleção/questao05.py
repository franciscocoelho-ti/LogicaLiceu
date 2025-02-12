# Escreva um algoritmo que leia 4 valores: valor_p, valor_a, valor_b e valor_c. Se valor_p for igual a 1 então calcular a média aritmética de  valor_a, valor_b e valor_c e escreva esta média; se valor_p for igual a 2 então somar os 3 valores atribuindo este valor a uma variável qualquer e escrevendo esta soma; se valor_p for igual a 3 então fazer um teste para saber se valor_b é par, se é par escrever a mensagem e o valor, caso contrário escrever que é ímpar. Se for qualquer outro valor mostrar a mensagem “operação inválida”.


# Entrada de Valores
# Ler: valor_p, valor_a, valor_b e valor_c

valor_p = int(input('Informe o valor de P: '))
valor_a = int(input('Informe o valor de A: '))
valor_b = int(input('Informe o valor de B: '))
valor_c = int(input('Informe o valor de C: '))

if valor_p == 1:
    media = (valor_a + valor_b + valor_c) / 3
    print('A média aritmética dos valores foi', media)

elif valor_p == 2:
    soma = valor_a + valor_b + valor_c
    print('O resultado da soma dos valores foi: ', soma)

elif valor_p == 3:
    if valor_b % 2 == 0:
        print('O valor de B é PAR')
    else:
        print('O valor de B é IMPAR')
        
else:
    print('Opção Inválida.')

